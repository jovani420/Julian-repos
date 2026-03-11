import psycopg2


conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='localhost',
    port='5432',
    database='db_alumnos'
)

print("Conexion activa")

cursor = conexion.cursor()

comando = "select * from alumno"

cursor.execute(comando)

db = cursor.fetchall()

for tabla in db:
    print(tabla)

cursor.close()
conexion.close()



