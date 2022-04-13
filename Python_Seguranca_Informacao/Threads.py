from threading import Thread #da biblioteca Threading estamos chamanoo a classe Thread
import time # importa a biblioteca time

def carro (velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5) # Espera 0,5 segundos para prosseguir com execução
        print('Piloto: {} Km: {} \n'.format(piloto, trajeto))



t_carro1 = Thread(target=carro, args=[1,'Bruno']) #Usa a Classe Thread da biblioteca threading, para executar carro
#Parametros 1° função, 2° argumentos da função
t_carro2 = Thread(target=carro, args=[2,'Python'])

t_carro1.start() #inicializa a chamada da função t_carro
t_carro2.start()