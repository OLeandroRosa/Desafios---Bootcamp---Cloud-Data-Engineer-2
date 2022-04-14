# Desafio
# Você terá o desafio de ler um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma loja,
# e informe-o expresso no formato horas:minutos:segundos.
#
# Entrada
# O arquivo de entrada contém um valor inteiro N.
#
# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

segundos = int(input('informe os segundos'))
horas = segundos // 3600  # Divide os segundos informados, pegando a parte inteira da divisão e convertendo para horas
segs_restantes = segundos %3600
minutos = segs_restantes//60 #TO.DO Implementar a formula para calcular os minutos.
segs_restantes_final = segs_restantes % 60

print("{}:{}:{}".format(horas, minutos, segs_restantes_final))

