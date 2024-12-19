import sqlite3
import os

def list_tables(db_file):
    """Lists all tables in a given SQLite database file.
    Args:
        db_file (str): The path to the SQLite database file.
    """

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("las tablas son")
    for table in tables:
        print(table[0])
    conn.close()

def list_tables_and_columns(db_file):
    """Lists all tables and their columns in an SQLite database.
    Args:
        db_file (str): Path to the SQLite database file.
    """
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Get a list of all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_names = cursor.fetchall()

    for table_name in table_names:
        table_name = table_name[0]
        print(f"\nTable: {table_name}")
        # Get column names for the current table
        cursor.execute(f"PRAGMA table_info('{table_name}')")
        columns = cursor.fetchall()
        for column in columns:
            column_name = column[1]
            data_type = column[2]
            print(f"  - {column_name} ({data_type})")
    conn.close()

# insertar Comarques 
def inserta_Comarca(conn, cursor,nombre_archivo):
    directorio_actual = os.getcwd()
    ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
    sqlsentence = f"""INSERT INTO Comarca
    (pk_com, nom_com) 
    VALUES (?, ?)"""
    with open(ruta_archivo, "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(";")
            print(data[0],data[1])
            cursor.execute(sqlsentence, (data[0],data[1]))
            conn.commit()

# insertar Provicias 
def inserta_Provicias(conn, cursor,nombre_archivo):
    directorio_actual = os.getcwd()
    ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
    sqlsentence = f"""INSERT INTO Provincias
    (pk_pro, nom_pro) 
    VALUES (?, ?)"""
    with open(ruta_archivo, "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(";")            
            print(data[0],data[1])
            cursor.execute(sqlsentence, (data[0],data[1]))
            conn.commit()


# insertar Comarque y provicias
def inserta_Comarca_provincias(conn, cursor,nombre_archivo):
    directorio_actual = os.getcwd()
    ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
    sqlsentence = f"""INSERT INTO Comarca_provincias
    (pk_cam_pro, fk_com_id, fk_pro_id) 
    VALUES (?, ?, ?)"""    
    with open(ruta_archivo, "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(";")            
            print(data[0],data[1],data[2])
            cursor.execute(sqlsentence, (data[0],data[1],data[2]))
            conn.commit()


# insertar Municipios
def inserta_Municipios(conn, cursor,nombre_archivo):
    directorio_actual = os.getcwd()
    ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
    sqlsentence = f"""INSERT INTO Municipios
    (pk_mun, nom_mun, fk_com_id) 
    VALUES (?, ?, ?)"""
    with open(ruta_archivo, "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(",")            
            print(data[0],data[1],data[2])
            cursor.execute(sqlsentence, (data[0],data[1],data[2]))
            conn.commit()

# insertar vias
def inserta_vias(conn, cursor, nombre_archivo):
    directorio_actual = os.getcwd()
    ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
    # TipoVia estamal declarado en el modelo
    sqlsentence = f"""INSERT INTO Tipo_via
    (pk_via, nom_via) 
    VALUES (?, ?)"""    
    try: # Código que puede generar un error ... 
        with open(ruta_archivo, "r", encoding='utf-8') as file:
            for line in file:
                data = line.strip().replace('"','').split(";")            
                print(data[0],data[1])
                cursor.execute(sqlsentence, (data[0],data[1]))
                conn.commit()
    except Exception as e:
        print(f"Error: {e}") 
        os.system("pause")


#directorio_actual = os.getcwd()
#nombre_archivo = "01_comarques.csv"
#ruta_archivo = os.path.join(directorio_actual, nombre_archivo)

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

nombre_archivo = "01_comarques.csv"
#inserta_Comarca(conn, cursor,nombre_archivo)

nombre_archivo = "01_comarques.csv"
#inserta_Provicias(conn, cursor,nombre_archivo)

nombre_archivo = "04_Comarca_provincias.csv"
#inserta_Comarca_provincias(conn, cursor,nombre_archivo)

nombre_archivo = "02_municipis.csv"
#inserta_Municipios(conn, cursor,nombre_archivo)

nombre_archivo = "05_tipo_via.csv"
inserta_vias(conn, cursor, nombre_archivo)


os.system("pause")
conn.close()

#
