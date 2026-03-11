import psycopg2


def update_persona():
    try:
        conexion = psycopg2.connect(
            user='postgres',
            password='admin',
            host='localhost',
            port='5432',
            database='db_personas'
        )
        with conexion.cursor() as c:
            query_only = """UPDATE persona 
                            SET nombre=%s, apellido_paterno=%s, apellido_materno=%s, edad=%s, correo=%s, universidad=%s 
                            WHERE id_persona=%s"""
            valor = ("Maria", "de los angeles", "Nes", 45, "television@ues.mx", "UES", 1)
            c.execute(query_only, valor)
            conexion.commit()
            print("\n Se edito con exito!")

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

def update_many_personas():
    try:
        conexion = psycopg2.connect(
            user='postgres',
            password='admin',
            host='localhost',
            port='5432',
            database='db_personas'
        )
        with conexion.cursor() as c:
            query_only = """UPDATE persona
                            SET nombre=%s, \
                                apellido_paterno=%s, \
                                apellido_materno=%s, \
                                edad=%s, \
                                correo=%s, \
                                universidad=%s
                            WHERE id_persona = %s"""
            valor = (("Antonio", "suift", "Johnson", 45, "Antonio@ues.mx", "UES",6),
                     ("Pepita", "Apodaca", "Mendez", 34, "operacion@ues.mx","UES",5),
                     ("Salomon", "Ruiz", "Aleman", 16, "iu@ues.mx", "UES",4)
                     )
            c.executemany(query_only, valor)
            conexion.commit()

            print("\n Se edito con exito!")

    except Exception as error:
        print(error)


while True:
    print("[1] - Editar individuo")
    print("[2] - Editar multiple")
    print("[3] - Mostrar")
    opcion = int(input("Ingrese su opcion: "))
    if opcion == 1:
        update_persona()
    if opcion == 2:
        update_many_personas()
    if opcion == 3:
        mostrar_personas()





