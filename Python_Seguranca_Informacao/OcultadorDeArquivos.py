import ctypes # biblioteca

pasta = input("digite o caminha da pasta a ser ocultadas, exemplo (C:/pasta): ")

atributo_ocultar = 0x02 # determina qual sera o atributo do arquivo oculto

retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt',atributo_ocultar) #chama na biblioteca ctype a DLL que  permite o que o arquvo seja manipulado e se torne oculto
#retorna True ou False

if retorno:
    print("arquivo ocultado")
else:
    print("arquivo nao oculado")
