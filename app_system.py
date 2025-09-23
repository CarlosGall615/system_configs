import customtkinter as ctk

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Sistema Teste')
app.geometry('940x500')

# Functions

def switch_event():
    print(f"switch toggled, current value: {alterar_dominio.get()}")
    print(f"switch toggled, current value: {remover_produtos.get()}")
    print(f"switch toggled, current value: {editar_produtos.get()}\n")
    

frame_head = ctk.CTkFrame(app, width=920, height=80, fg_color="#FFDFA1")
frame_head.place(x=10, y=10)

frame_menu = ctk.CTkFrame(app, width=140, height=400, fg_color="#FFDFA1")
frame_menu.place(x=10, y=100 )
frame_menu.pack_propagate(False)

frame_home = ctk.CTkFrame(app, width=770, height=400, fg_color="#FFFFFF")
frame_home.place(x=160, y=100)
frame_home.pack_propagate(False)

tabela = ctk.CTkTabview(frame_home, width=770, height=400, fg_color="#FFDFA1", bg_color="#FFDFA1",
                        segmented_button_fg_color='#FFDFA1',
                        segmented_button_selected_color="#FFFFFF",
                        segmented_button_selected_hover_color='#ababab',
                        segmented_button_unselected_color='#FFFFFF',
                        segmented_button_unselected_hover_color='#ababab',
                        text_color="#2D2D2D",

                        )
tabela.pack()
tabela.add("Permissões")
tabela.add("Servidor Local")
tabela.add("Domínio WEB")

alterar_dominio = ctk.StringVar(value="off")
switch = ctk.CTkSwitch(frame_home, text=" Alterar Dominio ", command=switch_event,
                            variable=alterar_dominio, onvalue="on", offvalue="off",
                            progress_color='green',
                            text_color="#2D2D2D",
                            fg_color="#ababab",
                            button_color="#FFFFFF",
                            button_hover_color="#ababab",
                            )
switch.place(x=170, y=130)

remover_produtos = ctk.StringVar(value="off")
switch = ctk.CTkSwitch(frame_home, text=" Remover Produtos ", command=switch_event,
                            variable=remover_produtos,
                            onvalue="on", offvalue="off",
                            progress_color='green',
                            text_color="#2D2D2D",
                            fg_color="#ababab",
                            button_color="#FFFFFF",
                            button_hover_color="#ababab",
                            )
switch.place(x=170, y=160)

editar_produtos = ctk.StringVar(value="off")
switch = ctk.CTkSwitch(frame_home, text=" Editar Produtos ", command=switch_event,
                            variable=editar_produtos,
                            onvalue="on", offvalue="off",
                            progress_color='green',
                            text_color="#2D2D2D",
                            fg_color="#ababab",
                            button_color="#FFFFFF",
                            button_hover_color="#ababab",
                            )
switch.place(x=170, y=190)
switch.pack_propagate(False)

label_dominio = ctk.CTkLabel(frame_home, text='Link do Seu PDV', text_color='green')
label_dominio.place(x=170, y=220)

label_http = ctk.CTkLabel(frame_home, text='HTTPS://', text_color='#2D2D2D', font=('arial bold', 20))
label_http.place(x=170, y=250)

input_label_http = ctk.CTkEntry(frame_home, placeholder_text='Seu dominio aqui')
input_label_http.place(x=285, y=250)

label_http2 = ctk.CTkLabel(frame_home, text='.dominio.com', text_color='#2D2D2D', font=('arial bold', 20))
label_http2.place(x=450, y=250)






app.mainloop()