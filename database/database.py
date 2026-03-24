import sqlite3

def conectar():
    return sqlite3.connect("banco.db")

def criar_tabela():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE,
        senha TEXT,
        is_admin INTEGER DEFAULT 0
    )
    """)

    cursor.execute(
        "UPDATE usuarios SET is_admin = 1 WHERE usuario = ?",
        ("maria123",)
    )


    conn.commit()
    conn.close()