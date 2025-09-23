import customtkinter as ctk

ctk.set_appearance_mode('dark')

usuarios = []

def validar_login():
    nome = campo_usuario.get()
    senha = campo_senha.get()

    for u in usuarios:
        if u['usuario'] == nome and u['senha'] == senha:
            validacao_login.configure(app, text='Login Efetuado com Sucesso!', text_color='green')
        else:
            validacao_login.configure(app, text='Dados Inválidos. Tente Novamente.', text_color='red')  



def abrir_cadastro():
    
    cadastro = ctk.CTkToplevel()
    cadastro.title('Cadastro Usuário')
    cadastro.geometry('450x400')

    ctk.CTkLabel(cadastro, text='Usuário: ').pack(pady=(5, 10))
    entry_nome = ctk.CTkEntry(cadastro)
    entry_nome.pack()

    ctk.CTkLabel(cadastro, text='Senha: ').pack(pady=(5,10))
    entry_senha = ctk.CTkEntry(cadastro)
    entry_senha.pack()

    def salvar_dados():

        nome  = entry_nome.get()
        senha = entry_senha.get()
        usuarios.append({'usuario': nome, 'senha': senha})
        
        print('Salvei')
        print(nome, senha)
        cadastro.destroy()
        
    btn_cadastro = ctk.CTkButton(cadastro, text='Salvar', command=salvar_dados)
    btn_cadastro.pack(pady=10)
    

    cadastro.mainloop()


app = ctk.CTk()
app.title('Sistema Teste')
app.geometry('500x800')


label_usuario = ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=5)

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu E-mail')
campo_usuario.pack(pady=5)

label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=5)

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite seu E-mail')
campo_senha.pack(pady=5)

btn_login = ctk.CTkButton(app, text='ENTRAR',text_color='white', command=validar_login)
btn_login.pack(pady=10)

validacao_login = ctk.CTkLabel(app, text='')
validacao_login.pack(pady=5)


btn_criar_conta = ctk.CTkButton(app, text='Criar Conta', text_color='white', command=abrir_cadastro)
btn_criar_conta.pack(pady=5)
print(btn_criar_conta)


app.mainloop()




