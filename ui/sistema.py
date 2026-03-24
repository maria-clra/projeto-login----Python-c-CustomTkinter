import customtkinter as ctk
from ui.adm import adm_cadastro


def sistema_adm(app):

    janela = ctk.CTkToplevel(app)
    janela.title("Sistema")
    janela.geometry("300x250")

    janela.grab_set()
    
    
    botao = ctk.CTkButton(
    janela,
    text="Administrador",
    command=lambda: adm_cadastro(app)
    )
    botao.pack(pady=10)

def sistema_user(app):

    janela = ctk.CTkToplevel(app)
    janela.title("Sistema")
    janela.geometry("300x250")

    janela.grab_set()
    
    
    botao = ctk.CTkButton(
    janela,
    text="......",
    )
    botao.pack(pady=10)