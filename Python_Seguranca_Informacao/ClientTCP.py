import socket # biblioteca faz a relacao entre a placa de rede e o sistema operacional
import sys #fornece o acesso a algumas variaveis e funções com o interpretador em p'ython

# função Socket.metodo socket, passaremos parametros  do TIPO de conexão que queremos fazer
# 1° Parametro: Familia, 2° Tipo, 3° Protocolo
# socket.AF_INET - informa que usaremoso protocolo IP
# socket.SOCK_STREAM - Informa que usaremos o TCP
# parametro 0 - informa o protocolo que faz a comunicação com  o servidor, nesse caso o TCP

def main ():
    try: # tenta uma conexao TCP/IP
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    except socket.error as erro: #Cria a excessão da função socket.error, variavel 'erro' vai armazenar a mensagem de erro
        print('A Conexão falhou !!!')
        print('Erro: {}'.format(erro))
        sys.exit() # Após o erro acontecer e aparecer as mensagens de erro, o comando sys.ext() fechara o programa
    print('Socket criado com sucesso')

    HostAlvo = input('Digite o Host ou IP a ser conectado: ')
    PortaAlvo = input('Digite a porta a ser Conectada: ')

    try:
        s.connect((HostAlvo,int(PortaAlvo)))
        print('Cliente TCP Conectado com sucesso no Host: ' + HostAlvo + 'e na Porta: ' + PortaAlvo)
        s.shutdown(2) #fecha a conexão em dois segundos, para não fica em loop a conexão, se não
                        #o comando s.connect, ficara conectando constantemente
    except socket.error as erro:
        print('Não foi possivel conectar no Host: '+ HostAlvo + 'e na Porta: ' + PortaAlvo)
        print('Erro: {}'.format(erro))
        sys.exit()

if __name__ =='__main__':
    main()