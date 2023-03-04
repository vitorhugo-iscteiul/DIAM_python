def bubblesort(lista):
    for i in range(len(lista)):
        for a in range(0, len(lista) - i - 1):
            if lista[a] > lista[a + 1]:
                b = lista[a + 1]
                lista[a + 1] = lista[a]
                lista[a] = b
    return lista


def optimizedBsort(lista):
    for i in range(len(lista)):
        for a in range(0, len(lista) - i - 1):
            if lista[a] > lista[a + 1]:
                lista[a + 1], lista[a] = lista[a], lista[a + 1]
    return lista


if __name__ == '__main__':
    lista1 = [1, 23, 42, 63, 4, 16, 8, 94, 72, 45, 6]
    lista2 = [1, 23, 42, 63, 4, 16, 8, 94, 72, 45, 6]
    print(bubblesort(lista1))
    print(optimizedBsort(lista2))
