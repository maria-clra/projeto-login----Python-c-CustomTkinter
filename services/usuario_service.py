from database.database import conectar


def criar_usuario(usuario, senha):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
        (usuario, senha)
    )

    conn.commit()
    conn.close()


def verificar_login(usuario, senha):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario=? AND senha=?",
        (usuario, senha)
    )

    resultado = cursor.fetchone()

    conn.close()

    return resultado