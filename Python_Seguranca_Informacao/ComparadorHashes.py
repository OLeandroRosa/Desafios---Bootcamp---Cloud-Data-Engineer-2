import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

#ripemd160 hash de 160 bits
hash1 = hashlib.new('ripemd160')   #comando chama um construtor chamado New,
# recebe como parametro uma string com o nome do tipo de Hash que usaremos e armazena o resultado na variavel

hash1.update(open(arquivo1, 'rb').read()) #faz a conversão do arquivo para criptofia do hash escolido
#comando open(NomeArquivo, modo de exibição) - o parametro 'rb' é equivamente a leitura(read) em binario

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

print(hash1)
print(hash2)

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print('O hash dpr arquivo a.txt é: ', hash1.hexdigest())
    print('O hash dpr arquivo b.txt é: ', hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print('O hash dpr arquivo a.txt é: ', hash1.hexdigest())
    print('O hash dpr arquivo b.txt é: ', hash2.hexdigest())