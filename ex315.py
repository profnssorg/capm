

## Inicialização de variáveis

cigarros_fumados_dia = int(0) # inicialização da variável que armazena o número de cigarros fumados.

anos_fumando =  int(0) # inicialização da variável que armazena o número de anos fumados

tempo_perda_vida_cigarro = int(10) # tempo medido em minutos, pois a perda é de 10 MINUTOS

dias_vida_perdido = float(0) # inicialização da variável



# Entrada de dados

anos_fumando = int(input("Quantos anos você fumou?\n"))

cigarros_fumados_dia = int(input("Quantos cigarros você fumava por dia?\n"))

# Processamento

""" O tempo de vida perdido é calculado multiplicando o número de cigarros pelo
tempo de vida perdido por cigarro como segue:

tempo_perdido = cigarros_fumados * tempo_perda_vida_cigarro

O número de dias perdidos é obtido dividindo o tempo_perdido por 1440 minutos que há
em um dia:

dias_vida_perdido = 365*anos_fumando*cigarros_fumados_dia*tempo_perda_vida_cigarro/1440

"""

dias_vida_perdido = 365*anos_fumando*cigarros_fumados_dia*tempo_perda_vida_cigarro/1440




#Saída

print("O fumante perdeu %f dias em sua vida."%dias_vida_perdido)
