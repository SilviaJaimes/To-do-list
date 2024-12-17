import streamlit as st
import mysql.connector
import json
import os

# Conexión a la db
def get_connection():
    return mysql.connector.connect(
        host="localhost", 
        port="3306",
        user="root",
        password="12345678",
        database="task_manager"
    )

# CRUD
def add_task(title, description, status="pendiente"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, status) VALUES (%s, %s, %s)", (title, description, status))
    conn.commit()
    conn.close()

def list_tasks():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def mark_task_completed(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status='completada' WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()

def delete_completed_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE status='completada'")
    conn.commit()
    conn.close()

# Exportar e importar
def export_tasks(file_path):
    tasks = list_tasks()
    structured_tasks = []

    for task in tasks:
        structured_tasks.append({
            "title": task.get("title", "Sin título"),
            "description": task.get("description", ""),
            "status": task.get("status", "pendiente")
        })

    with open(file_path, 'w') as file:
        json.dump(structured_tasks, file, indent=4)
    print(f"Tareas exportadas correctamente a {file_path}")

def import_tasks(file_path):
    if not os.path.exists(file_path):
        print("El archivo especificado no existe.")
        return

    with open(file_path, 'r') as file:
        try:
            tasks = json.load(file)

            for task in tasks:
                if "title" in task and "description" in task and "status" in task:
                    add_task(task["title"], task["description"], task["status"])
                else:
                    print("Formato inválido en una tarea.")
        except json.JSONDecodeError:
            print("El archivo JSON tiene un formato incorrecto.")
            return
    print("Tareas importadas correctamente.")

# Streamlit
def main():
    st.title("Aplicación de gestión de tareas")
    
    menu = ["Agregar tarea", "Listar tareas", "Marcar completada", "Eliminar completadas", "Importar/Exportar"]
    choice = st.sidebar.selectbox("Menú", menu)
    
    if choice == "Agregar tarea":
        st.subheader("Agregar nueva tarea")
        title = st.text_input("Título")
        description = st.text_area("Descripción")
        if st.button("Agregar"):
            if title:
                add_task(title, description)
                st.success(f"tarea '{title}' agregada exitosamente.")
            else:
                st.error("El título no puede estar vacío.")
    
    elif choice == "Listar tareas":
        st.subheader("Lista de tareas")
        tasks = list_tasks()
        if tasks:
            for task in tasks:
                status = "✅" if task['status'] == 'completada' else "⏳"
                st.write(f"{status} **{task['title']}** - {task['description']}")
        else:
            st.info("No hay tareas disponibles.")

    elif choice == "Marcar completada":
        st.subheader("Marcar tarea como completada")
        tasks = list_tasks()
        task_options = {task['title']: task['id'] for task in tasks if task['status'] == 'pendiente'}
        selected_task = st.selectbox("Selecciona una tarea", list(task_options.keys()))
        if st.button("Marcar como completada"):
            mark_task_completed(task_options[selected_task])
            st.success(f"tarea '{selected_task}' marcada como completada.")

    elif choice == "Eliminar completadas":
        st.subheader("Eliminar tareas completadas")
        if st.button("Eliminar"):
            delete_completed_tasks()
            st.success("Tareas completadas eliminadas exitosamente.")

    elif choice == "Importar/Exportar":
        st.subheader("Importar o exportar tareas")
        
        export_path = st.text_input("Ruta para exportar (ej: tareas.json)")
        if st.button("Exportar"):
            if export_path:
                export_tasks(export_path)
                st.success("Tareas exportadas exitosamente.")
            else:
                st.error("Especifica una ruta válida.")
        
        import_file = st.file_uploader("Importar Archivo JSON", type=["json"])
        if import_file and st.button("Importar"):
            with open("temp.json", "wb") as f:
                f.write(import_file.read())
            import_tasks("temp.json")
            st.success("Tareas importadas exitosamente.")

if __name__ == "__main__":
    main()
