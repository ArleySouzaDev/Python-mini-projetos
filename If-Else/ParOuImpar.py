import math

num = int(input("Digite um número para saber se é par ou impar: "))
resto = num % 2

if resto == 0:
    print('Este número é par!!')
else:
    print("Este número é impar!!")
