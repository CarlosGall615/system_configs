import customtkinter as ctk
from tkinter import font
import webbrowser
from tkinter import messagebox, ttk
# ----------------------------------------------------
# Aparência 
ctk.set_appearance_mode('dark')

def abrir_home(usuario):
        app = ctk.CTk()
        app.title(' 🧑‍🍳 Configurações do Sistema')
        app.geometry('940x500')
        app.protocol("WM_DELETE_WINDOW", lambda: (app.destroy()))
        
# ---------------------------------------------------------
# Funções de funcionalidades

        def abrir_configurações():

                if messagebox.askyesno("Abrir Configurações?"):

                        tabela.pack()
                        guia_produtos.pack_forget()
                return    

        def fechar_home():
                if  messagebox.askyesno("Fechar Configurações?"):   
                        guia_produtos.pack_forget()         
                        tabela.pack_forget()
                        
                return
        
        def abrir_sistema():

                url = f"index.html"
                webbrowser.open(url)
        
        def sair():
                
                if messagebox.askyesno("Confirmação", "Deseja Sair?"):
                        app.destroy()
        

        def abrir_tab_criar_produtos():
                tabela.pack_forget()
                guia_produtos.pack()
                return

        


        def salvar_proutos():

                

                if messagebox.askyesno("Confirmação", "Salvar o Produto?"):

                        produtos = []

                        nome_produto = name_product.get()
                        preco_produto = preco_product.get()
                        categoria_produto = category_product.get()

                        if nome_produto and preco_produto and categoria_produto:

                                lista_produtos = (nome_produto, preco_produto, categoria_produto)
                                produtos.append(lista_produtos)

                                
                                
                                name_product.delete(0, 'end')
                                preco_product.delete(0, 'end')
                                category_product.delete(0, 'end')
                                print("Produto Salvo com Sucesso!")
                                


# ----------------------------------------------------------
# Layout de Frames Janela
        

        frame_head = ctk.CTkFrame(app, width=920, height=100, fg_color='SkyBlue4')
        frame_head.place(x=10, y=5)

        frame1 = ctk.CTkFrame(master=app,  width=150, height=380, fg_color='SkyBlue4')
        frame1.place(x=10, y=110)
        frame1.pack_propagate(False)

        frame_home = ctk.CTkFrame(app, width=765, height=380, fg_color='SkyBlue4')
        frame_home.place(x=165, y=110)
        frame_home.pack_propagate(False)

# --------------------------------------------------------------------
# Tabwiew com abas
        ctk.CTkLabel(frame_head, text=f"Bem-vindo, {usuario}!", font=("Arial", 18, "bold")).place(x=450, y=10)

        tabela = ctk.CTkTabview(frame_home, width=770, height=400, fg_color="SkyBlue4",
                                segmented_button_fg_color='SkyBlue4',
                                segmented_button_selected_color="#FFFFFF",
                                segmented_button_selected_hover_color='#ababab',
                                segmented_button_unselected_color='#FFFFFF',
                                segmented_button_unselected_hover_color='#ababab',
                                text_color="#2D2D2D",
                                bg_color="SkyBlue4",
                                corner_radius=20,
                                )
        tabela.add("Permissões")
        tabela.add("Servidor Local")
        tabela.add("Domínio WEB")
        tabela._segmented_button.configure(height=38)
        tabela._segmented_button.configure(font=("Arial", 14, "bold"))
        tabela.pack_forget()

        guia_produtos = ctk.CTkTabview(frame_home, width=770, height=400, fg_color="SkyBlue4",
                                segmented_button_fg_color='SkyBlue4',
                                segmented_button_selected_color="#FFFFFF",
                                segmented_button_selected_hover_color='#ababab',
                                segmented_button_unselected_color='#FFFFFF',
                                segmented_button_unselected_hover_color='#ababab',
                                text_color="#2D2D2D",
                                bg_color="SkyBlue4",
                                corner_radius=20
                                )
        guia_produtos.add("Cadastrar Produtos")
        guia_produtos.add("Produtos Cadastrados")
        guia_produtos.add("Estoque")      
        guia_produtos._segmented_button.configure(height=38)
        guia_produtos._segmented_button.configure(font=("Arial", 14, "bold"))
        guia_produtos.pack_forget()

        # ------------------------------------------------------------------
        # Frames da Tabwiew  


        frame_permissoes = tabela.tab("Permissões")
        frame_admin = ctk.CTkScrollableFrame(frame_permissoes, width= 210, fg_color="SkyBlue3",
                                        scrollbar_button_color="#ababab",
                                        scrollbar_button_hover_color="#FFFFFF")
        frame_admin.place(x=0, y=30)
        label_admin = ctk.CTkLabel(frame_permissoes, text="Administrador", font=("Arial", 14, "bold"))
        label_admin.place(x=69, y=0)

        frame_users = ctk.CTkScrollableFrame(frame_permissoes, width= 210, fg_color="SkyBlue3",
                                        scrollbar_button_color="#ababab",
                                        scrollbar_button_hover_color="#FFFFFF")
        frame_users.place(x=245, y=30)
        label_users = ctk.CTkLabel(frame_permissoes, text="Usuário", font=("Arial", 14, "bold"))
        label_users.place(x=335, y=0)

        frame_view = ctk.CTkScrollableFrame(frame_permissoes, width= 210, fg_color="SkyBlue3",
                                        scrollbar_button_color="#ababab",
                                        scrollbar_button_hover_color="#FFFFFF")
        frame_view.place(x=490, y=30)
        label_view = ctk.CTkLabel(frame_permissoes, text="Outros", font=("Arial", 14, "bold"))
        label_view.place(x=570, y=0,)


        frame_add_product = guia_produtos.tab("Cadastrar Produtos")
        frame_product = ctk.CTkFrame(frame_add_product, width=400, height=500, fg_color='SkyBlue3'
                                                )
        frame_product.place(x=10, y=30)

        frame_add_product_tabela = guia_produtos.tab("Produtos Cadastrados")
        frame_lista_produtos = ctk.CTkFrame(frame_add_product_tabela, width=800, height=500, fg_color='SkyBlue3')
        frame_lista_produtos.place(x=10, y=30)

        # ------------------------------------------------------------------
        # Botoes Switchs de * Permissoes Admin


        switch_admin_dominio = ctk.CTkSwitch(frame_admin,
                                text='Alterar Domínio',
                                command=lambda: print("Alterar Domínio: ", switch_admin_dominio.get()),
                                onvalue="on", offvalue="off",
                                progress_color='green')
        switch_admin_dominio.pack(anchor="sw", pady=10, padx=10)


        switch_admin_servidor = ctk.CTkSwitch(frame_admin,
                                text='Alterar Servidor Local',
                                command=lambda: print("Alterar Servidor Local: ", switch_admin_servidor.get()),
                                onvalue="on", offvalue="off",
                                progress_color='green')
        switch_admin_servidor.pack(anchor="sw", padx=10)


        switch_admin_editar = ctk.CTkSwitch(frame_admin,
                                text='Editar Usuários',
                                command=lambda: print("Editar Usuários: ", switch_admin_editar.get()),
                                onvalue="on", offvalue="off",
                                progress_color='green')
        switch_admin_editar.pack(anchor="sw", pady=10, padx=10)


        switch_admin_logs = ctk.CTkSwitch(frame_admin,
                                text='Gerar Logs de Sistema',
                                command=lambda: print("Gerar Logs de Sistema: ", switch_admin_logs.get()),
                                onvalue="on", offvalue="off",
                                progress_color='green')
        switch_admin_logs.pack(anchor="sw", padx=10)


        switch_admin_hardwares = ctk.CTkSwitch(frame_admin,
                                text='Alterar Configurações\nde Hardwares',
                                command=lambda: print("Editar Hardwares: ", switch_admin_hardwares.get()),
                                onvalue="On", offvalue="Off",
                                progress_color='green')
        switch_admin_hardwares.pack(anchor="sw", pady=10, padx=10)


        switch_admin_cancelar_cupons = ctk.CTkSwitch(frame_admin,
                                text='Cancelar Cupons',
                                command=lambda: print("Cancelar Cupons: ", switch_admin_cancelar_cupons.get()),
                                onvalue="on", offvalue="off",
                                progress_color='green')
        switch_admin_cancelar_cupons.pack(anchor="sw", padx=10)


        switch_admin_descontos = ctk.CTkSwitch(frame_admin,
                                text='Permitir Descontos',
                                command=lambda: print("Permitir Descontos: ", switch_admin_descontos.get()),
                                onvalue="On", offvalue="Off",
                                progress_color='green')
        switch_admin_descontos.pack(anchor="sw", pady=10, padx=10)

        switch_admin_excluir_vendas = ctk.CTkSwitch(frame_admin,
                                text='Excluir Vendas',
                                command=lambda: print("Excluir Vendas: ", switch_admin_excluir_vendas.get()),
                                onvalue="on", offvalue="off",
                                progress_color='green')
        switch_admin_excluir_vendas.pack(anchor="sw", padx=10)

        # ------------------------------------------------------------------
        # Botoes Switchs de * Permissoes Usuario


        switch_users_vendas = ctk.CTkSwitch(frame_users,
                                text='Registrar Vendas',
                                command=lambda: print("Registrar Vendas: ", switch_users_vendas.get()),
                                onvalue="On", offvalue="Off",
                                progress_color='green')
        switch_users_vendas.pack(anchor="sw", pady=10, padx=10)


        switch_users_descontos = ctk.CTkSwitch(frame_users,
                                text='Aplicar Descontos\nLimitados',
                                command=lambda: print("Aplicar Descontos Limitados: ", switch_users_descontos.get()),
                                onvalue="On", offvalue="Off",
                                progress_color='green')
        switch_users_descontos.pack(anchor="sw", padx=10)


        switch_users_caixa = ctk.CTkSwitch(frame_users,
                                text='Abrir/Fechar Caixa',
                                command=lambda: print("Abrir/Fechar Caixa: ", switch_users_caixa.get()),
                                onvalue="On", offvalue="Off",
                                progress_color='green')
        switch_users_caixa.pack(anchor="sw", pady=10, padx=10)


        switch_users_cadastro_clientes = ctk.CTkSwitch(frame_users,
                                text='Cadastrar Cliente',
                                command=lambda: print("Cadastrar Cliente: ", switch_users_cadastro_clientes.get()),
                                onvalue="On", offvalue="Off",
                                progress_color='green')
        switch_users_cadastro_clientes.pack(anchor="sw", padx=10)

        switch_users_buscar_produtos = ctk.CTkSwitch(frame_users,
                                text='Buscar Produtos',
                                command=lambda: print("Buscar Produtos: ", switch_users_buscar_produtos.get()),
                                onvalue="On", offvalue="Off",
                                progress_color='green')
        switch_users_buscar_produtos.pack(anchor="sw", pady=10, padx=10)



        switch_users_receber_pagamentos = ctk.CTkSwitch(frame_users,
                                text='Receber Pagamentos',
                                command=lambda: print("Receber Pagamentos: ", switch_users_receber_pagamentos.get()),
                                onvalue="On", offvalue="Off",
                                progress_color='green')
        switch_users_receber_pagamentos.pack(anchor="sw", padx=10)

        # ------------------------------------------------------------------
        # Botoes Switchs de * Permissoes Outros


        frame_servidor = tabela.tab("Servidor Local")
        button = ctk.CTkButton(frame_servidor, text='Configurar Servidor',
                                width=100,
                                fg_color="#FFFFFF",
                                text_color="#2D2D2D",
                                hover_color='#ababab',
                                font=('arial bold', 15))

        button.place(x=185, y=50)


        menu = ctk.CTkOptionMenu(frame_servidor,
                                values=["9005", "9003", "9008", "9070"],
                                        width=250,
                                        font=('arial bold', 15),
                                        height=35,
                                        button_color='#FFFFFF',
                                        fg_color='#FFFFFF',
                                        dropdown_fg_color='#2D2D2D',
                                        dropdown_font=('arial bold', 15),
                                        corner_radius=10,
                                        dropdown_hover_color='#ababab',
                                        text_color="#2D2D2D"
                                        )
        menu.place(x= 185, y=85)
        menu.set("Portas")


        frame_dominio = tabela.tab("Domínio WEB")
        label_dominio = ctk.CTkLabel(frame_dominio, text='Seu Domínio WEB atual: ',)
        label_dominio.place(x=175, y=50)

        label_http = ctk.CTkLabel(frame_dominio, text='HTTPS://', font=('arial bold', 14))
        label_http.place(x=175, y=85)

        input_label_http = ctk.CTkEntry(frame_dominio, placeholder_text='Seu dominio aqui', width=300)
        input_label_http.place(x=235, y=85)

        label_http2 = ctk.CTkLabel(frame_dominio, text='.dominio.com', font=('arial bold', 14))
        label_http2.place(x=535, y=85)

        btn_salvar_dominio = ctk.CTkButton(frame_dominio, text='Salvar', width=100,
                                        fg_color="#FFFFFF",
                                        text_color="#2D2D2D",
                                        hover_color='#ababab',
                                        )
        btn_salvar_dominio.place(x=430, y=125)

        btn_editar_dominio = ctk.CTkButton(frame_dominio, text='Editar', width=100,
                                        fg_color="#FFFFFF",
                                        text_color="#2D2D2D",
                                        hover_color='#ababab')
        btn_editar_dominio.place(x=310, y=125)

        # Botoes Menu:

        btn_abrir_permissoes = ctk.CTkButton(frame1, text='⚙️ Configurações\ndo Sistema',
                                             command=abrir_configurações)
        btn_abrir_permissoes.pack(pady=10)

        btn_home = ctk.CTkButton(frame1, text="Voltar",
                                 command=fechar_home)
        btn_home.pack()

        abrir_site = ctk.CTkButton(frame1, text="Abrir Sistema",
                                   command=abrir_sistema)
        abrir_site.pack(pady=10)

        btn_fechar = ctk.CTkButton(frame1, text="Sair",
                                   command=sair)
        btn_fechar.pack()
        
        btn_cadastro_produtos = ctk.CTkButton(frame1, text="Adicionar Produtos",
                                              command=abrir_tab_criar_produtos)
        btn_cadastro_produtos.pack(pady=10)
        ## ------------------
        # Aba Cadastro Produtos::

        label_name_product = ctk.CTkLabel(frame_product, text="Produto")
        label_name_product.place(x=20, y=10)
        name_product = ctk.CTkEntry(frame_product, placeholder_text="Ex: Produto 1", width=150)
        name_product.place(x=10, y=40)

        label_preco_product = ctk.CTkLabel(frame_product, text="Preço(R$)")
        label_preco_product.place(x=20, y=70)
        preco_product = ctk.CTkEntry(frame_product, placeholder_text="Ex: R$ 10,20", width=150)
        preco_product.place(x=10, y=100)

        label_category_product = ctk.CTkLabel(frame_product, text="Categoria:")
        label_category_product.place(x=20, y=130)
        category_product = ctk.CTkEntry(frame_product, placeholder_text="Ex: Bebidas", width=150)
        category_product.place(x=10, y=160)

        btn_salvar_product = ctk.CTkButton(frame_product, text='Salvar', command=salvar_proutos)
        btn_salvar_product.place(x=100, y=220)
        

        style = ttk.Style(app)

        style.configure("Treeview",
                        font=('arial bold', 14),
                        font_color='black',
                        backgound="SkyBlue4",
                        foregound='SkyBlue3',

                        )
        style.configure("colunas_tabela",
                        font=('arial bold', 14),
                        font_color='black')
        
        
        # comando para Iniciar Aplicação
        app.mainloop()




