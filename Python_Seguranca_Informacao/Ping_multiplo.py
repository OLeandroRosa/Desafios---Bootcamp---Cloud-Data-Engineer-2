#Programa usa um arquivo de texto para fazer o ping de diversos hosts ,
#O programa vai percorrer o arquivo de texto para pingar todos os host que estive no arquivo
import os
import time #trabalha com tempo de execução

with open('hosts.txt') as file: #Comando abre o documento como um arquivo
    dump = file.read() # armazena o conteudo do arquivo na veriavel
    dump=dump.splitlines() #Transforma as informações da várias em uma lista, separando as por LINHAS

for ip in dump:
    print('Verificando o ip: ', ip)
    print('-' * 60)
    os.system('ping -n 2 {}'.format(ip))
    #print(ip)
    print('-' * 60)
    time.sleep(5) #tempo de espera de um comando para o outro, 5 segundos de espera