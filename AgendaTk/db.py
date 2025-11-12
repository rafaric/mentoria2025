import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="newpassword",
        database="agenda_contactos",
    )


def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agenda (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50),
            apellido VARCHAR(50),
            telefono VARCHAR(20),
            email VARCHAR(100)
        )
    """)
    conn.commit()
    conn.close()


def insertar_contacto(nombre, apellido, telefono, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO agenda (nombre, apellido, telefono, email)
        VALUES (%s, %s, %s, %s)
    """, (nombre, apellido, telefono, email))
    conn.commit()
    conn.close()


def obtener_contactos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agenda ORDER BY apellido ASC")
    resultados = cursor.fetchall()
    conn.close()
    return resultados


def eliminar_contacto(id_contacto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM agenda WHERE id = %s", (id_contacto,))
    conn.commit()
    conn.close()
