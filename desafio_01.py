#1
# monthValue = int(input('Digite o número do mês: '))

# if monthValue > 12 or monthValue <= 0:
#     print('execute o codigo novamente digitando um número de 1 a 12')
#     exit()

# month_year = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December',}

# print(month_year[str(monthValue)])



#2

# text_value = len(input('Digite aqui o seu texto: '))
# print(text_value)

# if text_value <= 280:
#     print('TWEET')
# elif text_value > 280:
#     print('Esse texto é maior que o esperado.')

#3

age_value = int(input('Digite sua idade'))
weight_value = int(input('Digite seu peso'))
sleep_value = int(input('Quanto você dormiu nas últimas 24hrs'))

conditional_age = age_value >= 16 and age_value <= 69
conditional_weight = weight_value > 50
conditional_sleep = sleep_value >= 6

if conditional_age and conditional_weight and conditional_sleep:
    print('Você pode doar sangue')
else:
    print('Você não pode doar sangue')



