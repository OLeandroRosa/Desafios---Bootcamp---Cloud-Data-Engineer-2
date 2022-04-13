import socket # biblioteca faz a relacao entre a placa de rede e o sistema operacional
import sys #fornece o acesso a algumas variaveis e funções com o interpretador em p'ython

#Protocolo UDP Contempla o principio da disponibilidade da segurança de dados

# função Socket.metodo socket, passaremos parametros  do TIPO de conexão que queremos fazer

# Ordem dos parametro 1° Familia, 2° Tipo, 3° Protocolo
# socket.AF_INET - informa que usaremoso protocolo IP
# socket.SOCK_DGRAM- Informa que usaremos o UDP, IPv4 UDP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #variavel esta instanceando a função sokcet,
#criando um objeto de conexão na variavel 's'

print('Cliente Socket Criado com Sucesso !!!')
host = 'localhost'
porta = 5433
mensagem = ' Ola servidor firmeza?'

try:
   # print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(),(host, 5432)) #empacotando a mensagem em pacote UDP e enviando para o servidor
    #no host conforme variavel host e na porta 5432, que é onde o servidor vai estar "ouvindo"

    dados, servidor = s.recvfrom(4096) # recebe uma mensagem do servidor de até 4096 Bytes
    dados = dados.decode()
    print('Cliente: ' + dados)
finally:
    print('Cliente: fechando a conexão ')
    s.close() #fecha a conexão para nao deixar em looping