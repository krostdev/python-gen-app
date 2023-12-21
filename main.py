import customtkinter
import keyboard
import gen
from tkinter import messagebox

print("""
      

      




                                                     _  __        ___ _____    ___ ___ _  _ 
                                                    | |/ /_ _ ___/ __|_   _|  / __| __| \| |
                                                    | ' <| '_/ _ \__ \ | |   | (_ | _|| .` |
                                                    |_|\_\_| \___/___/ |_|    \___|___|_|\_|
                                                                            

                                                      GERADOR CRIADO POR KROST | EXECUTAVEL 
""")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x400")

app.iconbitmap("assets/logoapp.ico")

app.title("AD GEN | APP")

def loginEvent():
    email = user.get()
    passI = password.get()

    if email == "admin" and passI == "admin":
        app.destroy()
        gen.genwindow()

        print("Logado com sucesso")
    elif email == "user" and passI == "user":
        app.destroy()
        gen.genwindow()

        print("Logado com sucesso!")
    elif email == "" and passI == "":
        messagebox.showwarning("Dados Invalidos", "Insira dados validos em Usuario, e senha!")
    else:
        messagebox.showwarning("Conta não encontrada", "Esta conta não foi encontrada!")

text = customtkinter.CTkLabel(app, text="Fazer Login | Ad Gen App", font=("Open Sans", 20))
text.pack(padx=10, pady=10)

user = customtkinter.CTkEntry(app, placeholder_text="Digite seu usuario", font=("Helvetica", 14), corner_radius=4)
user.pack(padx=10, pady=10)

password = customtkinter.CTkEntry(app, placeholder_text="Digite sua senha", show="*", font=("Helvetica", 14), corner_radius=4)
password.pack(padx=10, pady=10)

login = customtkinter.CTkButton(app, text="Login", command=loginEvent)
login.pack(padx=10, pady=10)

app.mainloop()