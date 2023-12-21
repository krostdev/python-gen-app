import asyncio
import customtkinter as ctk
from tkinter.messagebox import showinfo
from tkinter import messagebox
import random

def genwindow():
    genapp = ctk.CTk()
    genapp.geometry("650x280")
    genapp.iconbitmap("assets/logoapp.ico")

    accv = ctk.StringVar()
    accv.set("A conta aparecerá aqui")

    def gerar():
        accType = selectacc.get().lower().split("-")[0]

        if accType == "":
            messagebox.showwarning(
                title="Selecione uma conta!",
                message="Selecione uma conta para ser gerada!"
            )
        else:
            with open(f"accounts/{accType}.txt") as file:
                lines = file.read().splitlines()

                if len(lines) == 0:
                    showinfo(
                            title="Sem estoque",
                            message=f"No momento não tem estoque da conta {accType}"
                        )
                elif len(lines) > 0:
                    with open(f"accounts/{accType}.txt") as file:
                            acc = random.choice(lines)
                                                    
                            lines.remove(acc)

                            with open(f"accounts/{accType}.txt", "w") as file:
                                file.write("\n".join(lines))
                            

                            accv.set(acc)

    acc_generated = ctk.CTkEntry(genapp, textvariable=accv, font=("Open Sans", 15), width=300, state="readonly").pack(pady=18)

    with open("accounts/disney.txt") as file:
        linesD = file.read().splitlines()
    
    with open("accounts/paramount.txt") as file:
        linesP = file.read().splitlines()

    selectacc = ctk.CTkComboBox(genapp, values=[f"Disney- {len(linesD)} Restantes", f"Paramount- {len(linesP)} Restantes"], width=230, state="readonly")
    selectacc.pack(padx=10, pady=15)
    btn_gen = ctk.CTkButton(genapp, text="Gerar", command=gerar).pack()

    genapp.mainloop()