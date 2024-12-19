# Gestión de tareas 📝
  
Aplicación que permite a los usuarios gestionar sus tareas diarias.

## Funcionalidades de la aplicación ⚙️

### Agregar tareas: 
  Permite al usuario agregar nuevas tareas con un título y una descripción.
### Listar tareas: 
  Muestra todas las tareas agregadas con su estado (pendiente o completada).
### Marcar tareas como completadas: 
  Permite al usuario marcar una tarea como completada.
### Eliminar tareas: 
  Permite al usuario eliminar tareas completadas.
### Guardar y cargar tareas: 
  Puede exportar las tareas en un archivo e importar las desde el mismo archivo.

## Herramientas utilizadas 🛠️ 
    Streamlit
    MySQL
    Sin Sonar

## Creación de la base de datos 📊

Crear la base de datos en MySQL con los siguientes comandos:

```bash
    CREATE DATABASE task_manager;

    USE task_manager;
    
    CREATE TABLE tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        status ENUM('pendiente', 'completada') DEFAULT 'pendiente'
    );
```

## Ejecución del proyecto 🔩

Instalar dependencias:

```bash
    pip install streamlit
    pip install mysql-connector-python
```

Ejecución:

```bash
    python -m streamlit run task_manager.py
```

## Muestras del proyecto 📽️

https://github.com/user-attachments/assets/6be5728e-e464-4474-a06a-36af21007e55
