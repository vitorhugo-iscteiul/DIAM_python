# 3.1 Exercício sobre strings

# Considere o poema “Corrente” de Chico Buarque:
# 1 - Imprima na consola os 5º e 6º versos do poema.
# 2 - Imprima na consola o poema formatado da seguinte forma:
# 3 - Junte a estrofe seguinte ao fim do poema:
# Por isso eu fiz um samba bem pra frente
# Dizendo realmente o que é que eu acho
# Isso me deixa triste e cabisbaixo
# 4 - Imprima na consola os dois últimos versos do poema
# na sua forma depois das alíneas 1, 2 e 3.

file = open('poema.txt', 'r', encoding='utf-8')

estrofe = ["Por isso eu fiz um samba bem pra frente","Dizendo realmente o que é que eu acho","Isso me deixa triste e cabisbaixo"]


def readfile():
    return file.read().split(' / ')

if __name__ == '__main__':

    poem = readfile()
    # 3.1 a)
    print("o 5º verso é o: " + poem[4])
    print('O 6º verso é o : ' + poem[5])

    print("\n")

    # 3.1 b)
    for x in poem:
         print(x)

    # 3.1 c)
    poemafinal = poem + estrofe

    print("\n")

    # 3.1 d)
    print(poemafinal[-2:])

    