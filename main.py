import tkinter as tk
from tkinter import *
import qrcode


#interface grafica

Window = tk.Tk()
Window.geometry('1000x1000')
Window.title = 'Gerador de QR Code'
Window.config(bg='red')

FrameMain = tk.Frame(Window)
FrameMain.pack()

TitleInput = tk.Label(FrameMain, text='Coloque seu URL aqui', font=('Arial', 40))
TitleInput.pack(pady=10)

InputUrl = tk.Entry(FrameMain)
InputUrl.pack(pady=10)
InputUrl.config(width=500, font=('Arial', 40))

def gerarqr():
    Url = InputUrl.get()
    img = qrcode.make(Url)
    img.save('QrCode.png')
    alertlabel = tk.Label(FrameMain, text='Arquivo gerado com sucesso!, olhe seus arquivos')
    alertlabel.pack(pady=10)


ButtonGerar = tk.Button(FrameMain, text='Gerar', font=('Arial', 40), command=gerarqr)
ButtonGerar.pack(pady=10)

Window.mainloop()