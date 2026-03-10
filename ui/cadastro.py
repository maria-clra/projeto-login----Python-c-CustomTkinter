import customtkinter as ctk
from services.usuario_service import criar_usuario


def abrir_cadastro(app):

    janela = ctk.CTkToplevel(app)
    janela.title("Cadastro")
    janela.geometry("300x250")

    label_user = ctk.CTkLabel(janela, text="Novo usuário")
    label_user.pack(pady=5)

    entry_user = ctk.CTkEntry(janela)
    entry_user.pack(pady=5)

    label_senha = ctk.CTkLabel(janela, text="Senha")
    label_senha.pack(pady=5)

    entry_senha = ctk.CTkEntry(janela, show="*")
    entry_senha.pack(pady=5)

    resultado = ctk.CTkLabel(janela, text="")
    resultado.pack(pady=5)

    def cadastrar():

        usuario = entry_user.get()
        senha = entry_senha.get()

        criar_usuario(usuario, senha)

        resultado.configure(text="Usuário criado!", text_color="green")

    botao = ctk.CTkButton(janela, text="Cadastrar", command=cadastrar)
    botao.pack(pady=10)