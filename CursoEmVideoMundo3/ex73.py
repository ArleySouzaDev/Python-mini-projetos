#Crie um tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação, 
#Depois Mostre:
#A) Apenas os 5 primeiros colocados.
#B) Os últimos 4 colocados da tabela
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time da Chapecoense.

times = ("Flamengo","Vasco","Botafogo","Fluminense","Chapecoense","São Paulo","Palmeiras","Corinthians","Asa Branca","Bahia","Curitiba",
         "Vitória","Remo","Avaí","Ponte Preta","Santos","Internacional","Cruzeiro","Grêmio","Atlético Mineiro")

print("-=" *  15)
print(f"Lista de times:  {times}")
print("-=" *  15)
print(f"Os 5 primeiros são {times[0:5]}")
print("-=" * 15)
print(f"Os 4 últimos são {times[-4:]}")
print("-=" * 15)
print(f"Times em ordem alfabética: {sorted(times)}") 
print("-=" * 15)
print(f"O Chapecoense está na {times.index('Chapecoense')+1}ª posição")

