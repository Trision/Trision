import tkinter as tk
from tkinter import *
from tkinter.ttk import Label
from tkinter import ttk
import os
from gcpstorage import StorageGCP



janela = tk.Tk()
gcp = StorageGCP()

#configuração da janela
janela.title("Baixar arquivos")
janela.geometry('250x150+650+350')
janela.resizable(False, False)
janela.iconbitmap('logo.ico')
janela.configure(bg="#F9FCFE")

#menu e config de tamanho
carteiras = ('arquivo1', 'arquivo2', 'arquivo3')
cart = tk.StringVar()
paddings = {'padx': 5, 'pady': 5}


#Variaveis
label = Label(janela, text="Contrato: ", background="#F9FCFE")
label.grid(column=0, row=0, sticky=tk.W,**paddings)
text = Entry(janela, bg="#F9FCFE")
text.grid(column=1, row=0, sticky=tk.W, **paddings)
text.focus()
label3 = Label(janela, text="Carteira: ", background='#F9FCFE')
label3.grid(column=0, row=2, sticky=tk.W,**paddings)
carteira = ttk.OptionMenu(janela, cart, 'selecione', *carteiras)
carteira.grid(column=1, row=2, sticky=tk.W, **paddings)


#def para baixar
def baixar():
    carteira = cart.get().lower() # or .replace("text to be change", "new text")
    cont = text.get().replace(" ", "")
    user = os.getlogin()
    fonte = ['arquivo1', 'arquivo2', 'arquivo3']
    for item in fonte:
        if carteira == item:
            fonte = item
    if fonte == 'arquivo1':
        tipo = 'zip' #por conta dos arquivos vinculados ao arquivo1 estarem em zip no google cloud
    else:
        tipo = 'pdf' #os arquivos vinculados aos arquivos 2 e 3 estão em pdf
    PATH = f"C:\\Users\\{user}\\Desktop\\pastaExemplo"
    isExist = os.path.exists(PATH)
    if not isExist:
        print(f"Criando diretório {PATH}")
        os.makedirs(PATH)
        gcp.download(f"/contrato/{fonte}/{cont}.{tipo}", f"{PATH}/{cont}.{tipo}")
    else:
       gcp.download(f"/contrato/{fonte}/{cont}.{tipo}", f"{PATH}/{cont}.{tipo}")
    

#botão pra baixar
baixa = ttk.Button(janela, text="Baixar", command=baixar) #fg="white", bg='blue')
baixa.grid(column=1, row=3, sticky=tk.W, padx=20, pady=5)

cr = Label(janela, text="", background='#F9FCFE')
cr.grid(column=0, row=4, sticky=tk.W,**paddings)

cred = Label(janela, text="Desenvolvido por Luiz Fernando/Anderson", background='#F9FCFE')
cred.grid(column=0, row=5, columnspan=100, sticky=tk.W, padx=10)

janela.mainloop()

