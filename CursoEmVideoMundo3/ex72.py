#Crie um programa que tenha uma tupla, totalmente preenchida com uma contagem por extenso, de até vinte.

#seu programa deverá ler um número pelo teclado (0 e 20)
#e mostra-lo por extenso.

cont = ("zero", "um","dois","três","quatro","cinco","seis","sete","oito","nove",
        "dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","Zero",
        "dezenove","vinte",)



while True:    
    núm = int(input("Digite um número entre 0 e 20: "))
    if 0 <= núm <= 20:
        break
    print("Tente novamente. ", end='')

print(f"Você digitou o número {cont[núm]}")