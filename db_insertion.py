import psycopg2


def insert_persona():
    try:
        conexion = psycopg2.connect(
            user='postgres',
            password='admin',
            host='localhost',
            port='5432',
            database='db_personas'
        )
        with conexion.cursor() as c:
            query_only = "INSERT INTO persona (nombre, apellido_paterno, apellido_materno, edad, correo, universidad) VALUES (%s, %s, %s, %s, %s, %s)"
            valor = ("Natanael", "Cano", "Monguia", 78, "www@ues.mx", "UES")
            c.execute(query_only, valor)
            conexion.commit()

    except Exception as error:
        print(error)

def mostrar_personas():
    try:
        conexion = psycopg2.connect(
            user='postgres',
            password='admin',
            host='localhost',
            port='5432',
            database='db_personas'
        )
        with conexion.cursor() as c:
            query_only = "SELECT * FROM persona"
            c.execute(query_only)
            lista = c.fetchall()
            for i in lista:
                print(f"\n{i}")

    except Exception as error:
        print(error)

def insert_many_personas():
    try:
        conexion = psycopg2.connect(
            user='postgres',
            password='admin',
            host='localhost',
            port='5432',
            database='db_personas'
        )
        with conexion.cursor() as c:
            query_only = "INSERT INTO persona (nombre, apellido_paterno, apellido_materno, edad, correo, universidad) VALUES (%s, %s, %s, %s, %s, %s)"
            valor = (("Cesarin", "Cortez", "Palma", 45, "setenta@ues.mx", "UES"),
                     ("Cuatemok", "Ruiz", "Niz", 34, "op@ues.mx","UES"),
                     ("Rosa", "Sotomayor", "Aleman", 16, "suarez@ues.mx", "UES")
                     )
            c.executemany(query_only, valor)
            conexion.commit()

    except Exception as error:
        print(error)


while True:
    print("[1] - Insertar individuo")
    print("[2] - Insertar multiple")
    print("[3] - Mostrar")
    opcion = int(input("Ingrese su opcion: "))
    if opcion == 1:
        insert_persona()
    if opcion == 2:
        insert_many_personas()
    if opcion == 3:
        mostrar_personas()





