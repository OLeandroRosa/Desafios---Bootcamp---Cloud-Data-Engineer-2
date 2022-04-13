import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#variavel esta instanceando a função sokcet,
#criando um objeto de conexão na variavel 's'

print('Socket criado com sucesso')

host = 'localhost'
port = 5432

s.bind ((host, port)) #faz a ligação entre cliente e servidor atraves do host e da poorta

mensagem = '\nServidor: oláááááá Cliente, e aí Beleza?'

while 1:
    dados, end = s.recvfrom(4096) # armazena nas duas variaveis os dados recebido de até 4096 bytes
    #1° Variavel armazena a mensagem e a 2° variavel armazena o host e a porta
    #1° Variavel é da classe byte e a 2° variavel é uma tupla
    #print(dados, "e", end)
    #print(type(dados), 'e', type(end))


    if dados: # se a variave
        print('Servidor enviando mensagem ...')
        s.sendto(dados + (mensagem.encode()),end) #envia uma mensagem para o client,
        # mensagem é composta por 1° parametro = mensagem(texto), 2°Parametro o host e a porta



