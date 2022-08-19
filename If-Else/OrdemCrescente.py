primeiro = int(input("Digite o Primeiro número: "))
segundo = int(input("Digite o Segundo número: "))
terceiro = int(input("Digite o Terceiro número: "))



if (terceiro < segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

if (segundo < primeiro):
    aux = segundo
    segundo = primeiro
    primeiro = aux

if (terceiro < segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

print(primeiro, " - ", segundo, " - ", terceiro)
