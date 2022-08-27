#Crie um programa que tenha uma tupla única com os nomes dos produtos e seus respectivos preços na sequência.

#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ("Mochila", 120.00, "Bolsa", 300.00, "Pochete", 75.00, "Carteira", 100.00, "Porta-Moedas", 35.00)

print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"R${listagem[pos]:>7.2f}")
print("-" * 40)