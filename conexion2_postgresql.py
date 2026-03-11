import psycopg2


conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='localhost',
    port='5432',
    database='db_alumnos'
)

with conexion.cursor() as c:
    c.execute("SELECT * FROM persona")
    datos = c.fetchall()

    for dato in datos:
        print(dato)