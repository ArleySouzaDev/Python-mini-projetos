def éPrimo(k):

    divisores = 0
    for i in range(1,k):
        if k % i == 0:
            divisores += 1
    if divisores >= 2:
        return False
    else:
        return True


def maior_primo(n):
    maior_primo = 1

    for i in range(n + 1):
        if éPrimo(i) == True:
            maior_primo = i

    return maior_primo