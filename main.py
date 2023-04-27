import random

#importar pool de nombres
nombres_lista = ['María', 'José', 'Juan', 'Luis', 'Francisco', 'Karla', 'Nushi', 'Mohammed', 'Jose', 'Manuel', 'Antonio',
           'William', 'George', 'Joseph', 'Frank', 'Thomas', 'Carlos', 'Edward', 'Walter', 'Harold', 'Martín', 'Samuel',
           'Santiago', 'Sebastián', 'Alejandro', 'Jack', 'Donald', 'Albert', 'Paul', 'Daniel', 'David', 'Roy',
           'Kenneth', 'Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'William', 'Isabella', 'James', 'Sophia', 'Oliver',
           'Mia', 'Benjamin', 'Charlotte', 'Elijah', 'Amelia', 'Lucas', 'Harper', 'Mason', 'Evelyn', 'Logan', 'Abigail',
           'Alexander', 'Emily', 'Ethan', 'Elizabeth', 'Jacob', 'Mila', 'Michael', 'Avery', 'Daniel', 'Sofia', 'Henry',
           'Ella', 'Jackson', 'Scarlett', 'Sebastian', 'Grace', 'Aiden', 'Victoria', 'Matthew', 'Riley', 'Samuel',
           'Aria', 'David', 'Lily', 'Joseph']
apellidos_lista = ['Hernández', 'García', 'Martínez', 'López', 'González', 'Pérez', 'Rodríguez', 'Sánchez', 'Ramírez', 'Cruz',
             'Gómez', 'Flores', 'Morales', 'Vázquez', 'Jiménez', 'Reyes', 'Díaz', 'Torres', 'Gutiérrez', 'Ruiz',
             'Mendoza', 'Aguilar', 'Méndez', 'Moreno', 'Ortiz', 'Smith', 'Johnson', 'Williams', 'Jones', 'Brown',
             'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson',
             'Anderson', 'Taylor', 'Thomas', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White',
             'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson']

combinaciones = []

# Generar combinaciones
for i in range(35000):
    nombre = random.choice(nombres_lista)
    apellido1 = random.choice(apellidos_lista)
    apellido2 = random.choice(apellidos_lista)
    email = nombre + apellido1 + apellido2 + '@mail.com'
    combinaciones.append((nombre, apellido1, apellido2, email))

print(combinaciones)

# Crear archivo SQL
with open('alumnos.sql', 'w') as f:
    db_name = "sistema_escolar"
    # Escribir comando para crear base de datos si no existe
    f.write(f'CREATE DATABASE IF NOT EXISTS {db_name};\n')
    f.write(f'USE {db_name};\n')
    # Escribir comando para crear tabla
    f.write('''
        CREATE TABLE alumnos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            second_last_name varchar(255),
            email VARCHAR(255)
        );
    ''')

    # Escribir comandos para insertar datos
    for combination in combinaciones:
        f.write(f"INSERT INTO alumnos (first_name, last_name,second_last_name, email) VALUES ('{combination[0]}', '{combination[1]}', '{combination[2]}', '{combination[3]}');\n")
print('El script SQL ha sido guardado en el archivo scriptAlumnos.sql')