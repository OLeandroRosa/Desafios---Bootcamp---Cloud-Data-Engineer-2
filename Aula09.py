import shutil # shutil são fornecidas funções que possuem suporte a cópia e remoção de arquivos. Para operações em arquivos individuais
def escrever_arquivo(nome_arquvo,texto):
    diretorio = 'D:/Pycharm/PyCharm Community Edition 2021.3.3/Pycharm Projects/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n') # O Comando Split divide o texto conforme o parametro que colocamos e cria uma lista
    #print(aluno_nota)                   # no caso, a cada \n que ele encontrar, ele vai inserir um novo item na lista
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',') #Comando spli usado para separar o nome do alluno e as notas
        aluno = lista_notas[0] #Atribui a variavel Aluno o primeiro item da lista, que no caso é o nome do aluno
        lista_notas.pop(0) #Retira o primeiro elemento da lista, que no caso é o nome do aluno, afim de so restar as notas
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas])/4 # código Bootcamp, Rafael Galeani
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
        # -------------------------------- Meu código para calcular Média ------------------------------------
        # lista_notas_int = []
        # for i in lista_notas:
        #     lista_notas_int.append(int(i))
        # print('Lista Int Notas', lista_notas_int)
        # for x in lista_notas_int:
        #     soma = x+soma
        # media = soma/4
        # print('media', media)
        # soma = 0
        # -------------------------------- Final Meu código para calcular média -----------------------
    return lista_media

def copia_arquivo(nome_arquivo):

    shutil.copy(nome_arquivo, 'D:/Pycharm/PyCharm Community Edition 2021.3.3/Pycharm Projects/notas_novas.txt') #declarado parametro e local para cópia


def move_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'D:/Pycharm/PyCharm Community Edition 2021.3.3/')


if __name__ == '__main__':
    copia_arquivo('notas.txt')
    move_arquivo(('notas.txt'))
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    #escrever_arquivo('primeira linha. \n')
    # aluno = 'Galleani, 7, 9, 3, 8\n'
    # atualizar_arquivo('notas.txt',aluno)
    # atualizar_arquivo('terceira linha. \n')
    # ler_arquivo('teste.txt')