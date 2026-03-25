import customtkinter as ctk
import sqlite3


conn = sqlite3.connect("banco.db")
cursor = conn.cursor()


def inserir():
    usuario = entry_usuario.get()

    if not usuario:
        print("Digite um usuário")
        return
    
    cursor.execute(
        "INSERT INTO usuarios (usuario, senha, is_admin) VALUES (?, ?, ?)",
        (usuario, "00000", 0)
    )
    conn.commit()
    listar()

def excluir():
    id = entry_id.get()

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    listar()

def listar():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    textbox.delete("1.0", "end")

    for u in usuarios:
        textbox.insert("end", f"{u}\n")


def adm_cadastro(app):
    global entry_usuario, entry_id, textbox

    janela = ctk.CTkToplevel(app)
    janela.title("Administrador(a)")
    janela.geometry("300x250")

    janela.grab_set()

    botao_listar = ctk.CTkButton(janela, text='Listar', command=listar)
    botao_listar.pack(pady = 10)
    textbox = ctk.CTkTextbox(janela, width=250, height=50)
    textbox.pack(pady=10)

    
    entry_id = ctk.CTkEntry(janela, placeholder_text="ID para excluir")
    entry_id.pack(pady=5)
    botao_excluir = ctk.CTkButton(janela, text='Excluir', command=excluir)
    botao_excluir.pack(pady = 10)

    
    entry_usuario = ctk.CTkEntry(janela, placeholder_text="Usuário")
    entry_usuario.pack(pady=5)
    botao_inserir = ctk.CTkButton(janela, text='Inserir', command=inserir)
    botao_inserir.pack(pady = 10)

    

    


        