# Gestión de tareas 📝

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
