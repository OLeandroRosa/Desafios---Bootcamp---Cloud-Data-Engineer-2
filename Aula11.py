lista =[1,10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisão = 10 /1
    numero = lista[1]
    print('fechando arquivo')
    a=1
    x =a

except ZeroDivisionError: # Cria uma exceção para quando um erro de divisão por zero acontecer
    print('Não é possivel realizar uma divisão por 0')
except IndexError: # Cria uma exceção para quando o erro de indexador acontecer, então exibe uma frase diferente
    print('Erro ao acessar um indice inválido da lista')
except Exception as ex:  # A BaseException é o PAI/MESTRE de toda as outras exceções, depois dele que vem todas as outras exceções
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally: #Este comando SEMPRE executa, mesmo de acontecer algum erro na execução do programa.
    print('Sempre Executa')
    print('Fechando Arquivo')
    arquivo.close()

# as execeções são usadas para quando algum trecho do programa falha mas o programa em si não pode parar
# Durante a elaboração das exceções, deve ser colocado na parte de cima os FILHOS, as ultimas exceções da lista
# No final das exceções, deve ser colocado um Else para informar que não houve nenhuma exceção/ Erro