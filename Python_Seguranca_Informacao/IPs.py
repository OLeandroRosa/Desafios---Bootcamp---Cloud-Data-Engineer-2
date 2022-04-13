import ipaddress # Para manipular endereços de IP é necessário importar a biblioteca ipadress, bibliote nativa do p'ython3
#para podermos fazer calculos com IPs e Redes (Soma, subtração, divisão e multiplicação)

#ip = '192.168.0.1'
#endereço = ipaddress.ip_address(ip) # converte a string em ippadress, podendo fazer calculos com o resultado da variavel
#print(endereço + 2000)

ip = "192.168.0.0/0"

rede = ipaddress.ip_network(ip,strict=False) # quando usamoos o parametro strict=False, desligamos o monitoramento e aceitara qualquer rede

for ip in rede:
    print(ip)