import webbrowser
from tkinter import * #importa tudo da biblioteca

root = Tk( ) #objeto para representar o tkinter, espaço em branco representa a tela

root.title('Abrir Browser')
root.geometry('300x200') #tamanho da janela

def google():
    webbrowser.open('www.google.com') #informa o site que vai abrir

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20) #command chama a função que abre o google
#text parametro para informar o texto do botão, pack define a posição do botão e root chama a biblioteca tkinter

root.mainloop() #manter o programa rodando