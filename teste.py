from datetime import datetime, time

data_e_hora_atuais = datetime.now()


#invervalo = str(datetime.now())[10:-13]
invervalo = str(datetime.now())[10:16].split(':')
#invervalo = int(invervalo)

print(data_e_hora_atuais)
print(invervalo)
#if invervalo < 7:
 #   pass #print(invervalo)