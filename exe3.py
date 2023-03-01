def bubblesort(lista):
    for i in range(len(lista)):
        for a in range(0, len(lista)-i-1):
            if lista[a] > lista[a + 1]:
                b = lista[a + 1]
                lista[a + 1] = lista[a]
                lista[a] = b

if __name__ == '__main__':
    lista = [1, 3, 2, 3, 4, 6, 8, 4, 2, 45, 6]

    bubblesort(lista)
    print(lista)
