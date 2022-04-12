#Site para acessa a documentação da biblioteca:
#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
from datetime import date, time, datetime,timedelta

def trabalhando_com_datetime(): # Para usar a função datetime é necessário fazer a importação da função no cabeçalho do programa
    data_atual = datetime.now() # retorna a data e hora atual
    print(data_atual.strftime('%d/%m/%Y - %H:%M:%S')) #Formatando como deve ser exibido a data e hora
    print(data_atual.strftime('%c')) #ja formata a string, conforme documentação Exemplo: Tue Aug 16 21:30:00 1988
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20) #O comando esta criando uma data, sendo (ano, mes, dia, hora, minuto, segundo)
    print(data_criada)
    print(data_criada.strftime('%c'))
    #--------- para converter uma data em formato de String ----------
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    #----------- Trabalhando com a função timedelta, esta função deve ser declarada no cabeçalho do programa -------------
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)
    #------------ Fim do código trabalhando com a função Timedelta ---------------
def trabalhando_com_date():  # Para usar a função date é necessário fazer a importação da função no cabeçalho do programa
    data_atual = date.today() #Retorna a data de hoje
    data_atual_str = data_atual.strftime('%A %m %Y') #Conforme documentação, a função strftime, pode organizar as informações de data
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def tralhando_com_time():  # Para usar a função time é necessário fazer a importação da função no cabeçalho do programa
    horario=time(hour= 15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')#Conforme documentação, a função strftime, pode organizar as informações de hora
    print(horario.strftime('%H:%M:%S'))
    print(type(horario))
    print(type(horario_str))



if __name__ == '__main__':
    #trabalhando_com_date()
    #tralhando_com_time()
    trabalhando_com_datetime()
