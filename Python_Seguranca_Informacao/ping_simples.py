import os #Importa modulo ou biblioteca OS (integra os programas e recusos do sistema operacional

print('#' * 60) ## imprimindo # 60 vezes
ip_ou_host = input("Digite o IP ou HOst a ser verificado: ") #Variavel que recebe o IP/ host
print('-' * 60)## imprimindo - 60 vezes
os.system('ping -n 6 {}'.format(ip_ou_host)) #chamando o system da biblioteca os - comando ping
# -n -num de pacotes que serão o 6{}
print('-' * 60)  # e o comando ping é um deles