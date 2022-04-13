import hashlib

string = input ("Digite o teste a ser gerado a Hasg: ")
# resultado = hashlib.md5(b'P.ython Security') # o b no inicio da String transforma ela em bytes

menu = int(input(''' ### MENU - ESCOLHA O TIPO DE HASH ###
            1) MD5
            2) SHA1
            3) SHA256
            4) SHA512         
            Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8')) #Parametro utf-8, utilizado a tabela de caracteres pare encodificar a string
    print ('O hash MD5 da String é: ', string, 'é: ',resultado.hexdigest()) # imprime a string criptografda em MD5
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8')) #Parametro utf-8, utilizado a tabela de caracteres pare encodificar a string
    print ('O hash SHA1 da String é: ', string, 'é: ',resultado.hexdigest()) # imprime a string criptografda em MD5
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8')) #Parametro utf-8, utilizado a tabela de caracteres pare encodificar a string
    print ('O hash SHA256 da String é: ', string, 'é: ',resultado.hexdigest()) # imprime a string criptografda em MD5
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8')) #Parametro utf-8, utilizado a tabela de caracteres pare encodificar a string
    print ('O hash SHA512 da String é: ', string, 'é: ',resultado.hexdigest()) # imprime a string criptografda em MD5
else:
    print('Algo de errado não deu certo, tente novamente.')