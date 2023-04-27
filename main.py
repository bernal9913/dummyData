import random

nombres = ['María', 'José', 'Juan', 'Luis', 'Francisco', 'Maria', 'Nushi', 'Mohammed', 'Jose', 'Manuel', 'Antonio',
           'William', 'George', 'Joseph', 'Frank', 'Thomas', 'Carlos', 'Edward', 'Walter', 'Harold', 'Martín', 'Samuel',
           'Santiago', 'Sebastián', 'Alejandro', 'Jack', 'Donald', 'Albert', 'Paul', 'Daniel', 'David', 'Roy', 'Kenneth']
apellidos = ['Hernández','García','Martínez','López','González','Pérez','Rodríguez','Sánchez','Ramírez','Cruz','Gómez',
             'Flores','Morales','Vázquez','Jiménez','Reyes','Díaz','Torres','Gutiérrez','Ruiz','Mendoza','Aguilar',
             'Méndez','Moreno','Ortiz']

usuarios = []
for i in range(35000):
    nombre = random.choice(nombres)
    apellido1 = random.choice(apellidos)
    apellido2 = random.choice(apellidos)
    usuario = f'{nombre} {apellido1} {apellido2}'
    usuarios.append(usuario)

sql = "CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT);\n"
sql += "INSERT INTO usuarios (nombre) VALUES\n"
for usuario in usuarios:
    sql += f"('{usuario}'),\n"
sql = sql[:-2] + ";"

with open('scriptAlumnos.sql', 'w') as f:
    f.write(sql)

print('El script SQL ha sido guardado en el archivo scriptAlumnos.sql')