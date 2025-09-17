import customtkinter as ctk
import subprocess
import socket
import re 
# Aparência 
ctk.set_appearance_mode('dark')

# Funções de funcionalidades
#def selecionar_acao(choice):
    #if choice == "Testar Conexão":
       # print("Fui Chamado")
    #else:
        #textbox.configure(state="normal")
        #textbox.delete("1.0", "end")
        #textbox.insert("1.0", f"Ação selecionada: {choice}")
        #textbox.configure(state="disabled")

# Janela Principal
app = ctk.CTk()
app.title(' 🧑‍🍳 Configurações do Sistema')
app.geometry('940x500')

frame_head = ctk.CTkFrame(app, width=920, height=100, fg_color='SkyBlue4')
frame_head.place(x=10, y=5)

frame1 = ctk.CTkFrame(master=app,  width=150, height=380, fg_color='SkyBlue4')
frame1.place(x=10, y=110)
frame1.pack_propagate(False)

frame_home = ctk.CTkFrame(app, width=765, height=380, fg_color='SkyBlue4')
frame_home.place(x=165, y=110)
frame_home.pack_propagate(False)

# Campos de Informação (Label='' || Entry=''  || Button='')





tab_navegation = ctk.CTkTabview(frame_home, width=700, height= 280,
                                segmented_button_fg_color='SkyBlue4',
                                segmented_button_unselected_color='SkyBlue4',
                                segmented_button_unselected_hover_color='SkyBlue4',
                                segmented_button_selected_hover_color='SkyBlue4',
                                fg_color='SkyBlue3'
                                )
tab_navegation.pack()
tab_navegation.add("Geral")
tab_navegation.add("Servidor Local")
tab_navegation.add("Permissões")

button = ctk.CTkButton(frame1, text='Editar')
button.pack()




# comando para Iniciar Aplicação
app.mainloop()


#menu = ctk.CTkOptionMenu(frame_home,
                         #values=["Testar Conexão", "Renovar IP", "Limpar DNS", "Resetar Winsock",
                                 #"Corrigir Tudo"],
                                 #width=250,
                                 #font=('arial bold', 15),
                                 #height=35,
                                 #button_color='green',
                                 #fg_color='green',
                                 #dropdown_fg_color='SkyBlue4',
                                 #dropdown_font=('arial bold', 15),
                                 #corner_radius=10,
                                 #command=selecionar_acao
                                # )
#menu.pack(pady=5)
#menu.set("Escolha uma Opção")

#textbox = ctk.CTkTextbox(frame_home, width=350, height=350)
#textbox.pack(pady=10)