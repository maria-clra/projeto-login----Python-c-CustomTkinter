import customtkinter as ctk
from services.usuario_service import verificar_login
from ui.cadastro import abrir_cadastro
from ui.sistema import sistema_adm, sistema_user

#CustomTkinter = estiloso + profissional hehe
#Configuar a aparência 
ctk.set_appearance_mode('dark')

def iniciar_app():
    #Criação da janela principal
    app = ctk.CTk()
    app.title("Sistema de Login")
    app.geometry('300x300')

    def validar_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        resultado = verificar_login(usuario, senha)


        if resultado:

            tipo_usuario = "admin" if resultado[3] == 1 else "user"
            resultado_login.configure(text="Login realizado com sucesso")
            if tipo_usuario == "admin":
                sistema_adm(app)
            else:sistema_user(app)
        else:
            resultado_login.configure(text='Login incorreto!', text_color='red')

    #Criar campos
    label_usuario = ctk.CTkLabel(app, text='Usuário:')
    label_usuario.pack(pady=5)
    entry_usuario = ctk.CTkEntry(app, placeholder_text='digite seu usuário')
    entry_usuario.pack(pady=5)

    label_senha = ctk.CTkLabel(app, text='Senha:')
    label_senha.pack(pady=5)
    entry_senha = ctk.CTkEntry(app, placeholder_text='digite sua senha', show="*")
    entry_senha.pack(pady=5)


    # Button
    botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
    botao_login.pack(pady = 10)

    botao_cadastro = ctk.CTkButton(app, text="Criar conta", command=lambda: abrir_cadastro(app))
    botao_cadastro.pack(pady=5)

    app.bind("<Return>", lambda event: validar_login())
    
    #feedback
    resultado_login = ctk.CTkLabel(app,text='')
    resultado_login.pack(pady = 5)


    #iniar o app
    app.mainloop()