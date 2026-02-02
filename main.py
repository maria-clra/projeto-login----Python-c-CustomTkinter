import customtkinter as ctk
#CustomTkinter = estiloso + profissional hehe
#Configuar a aparência 
ctk.set_appearance_mode('dark')

#Criação das funções de funcionalidades

def validar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == 'maria123' and senha == '123456':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login incorreto!', text_color='red')
#Criação da janela principal
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry('300x300')
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

#feedback
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady = 5)

#iniar o app
app.mainloop()
