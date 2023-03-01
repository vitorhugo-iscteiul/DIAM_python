def bubblesort(lista):
    for i in range(len(lista)):
        for a in range(0, len(lista) - i - 1):
            if lista[a] > lista[a + 1]:
                b = lista[a + 1]
                lista[a + 1] = lista[a]
                lista[a] = b


def optimizedBsort(lista):
    for i in range(len(lista)):
        for a in range(0, len(lista) - i - 1):
            if lista[a] > lista[a + 1]:
                lista[a + 1], lista[a] = lista[a], lista[a + 1]


if __name__ == '__main__':
    lista1 = [1, 23, 42, 63, 4, 16, 8, 94, 72, 45, 6]
    lista2 = [1, 23, 42, 63, 4, 16, 8, 94, 72, 45, 6]
    bubblesort(lista1)
    print(lista1)
    optimizedBsort(lista2)
    print(lista1)
