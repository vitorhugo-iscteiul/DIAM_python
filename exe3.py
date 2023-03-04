# 3.3 Exercício de estruturas de controlo e listas
# Considere o algoritmo de ordenação de listas “Bubble
# Sort”. Este algoritmo percorre cada elemento de uma
# lista, compara-o com o elemento adjacente seguinte e
# troca os dois elementos se o primeiro for maior que o
# segundo. O procedimento é repetido até ordenar a lista.

# 1 - Programe o algoritmo “Bubble Sort”. Teste o seu
# programa.
# 2 - O seu programa pode ser optimizado com recurso às
# propriedades de Python. De facto, a maior parte das
# linguagens de programação exigem o processamento de
# três passos para a troca de valores entre dois elementos
# da lista (ver figura em baixo).
# Em Python essa troca pode ser feita numa única
# instrução. Por exemplo, a troca entre a e b pode ser feita
# com a instrução a,b = b,a .
# Optimize o seu programa para ordenar a lista com o
# mínimo possível de passos.
# Conte o tempo gasto para ordenar uma lista através de
# cada uma das suas versões do “Bubble Sort”. Qual é a
# mais rápida

def bubblesort(lista):
    for i in range(len(lista)):
        for a in range(0, len(lista) - i - 1):
            if lista[a] > lista[a + 1]:
                b = lista[a + 1]
                lista[a + 1] = lista[a]
                lista[a] = b
    return lista


def optimizedBsort(lista):
    counter = 0
    for i in range(len(lista)):
        counter += 1
        for a in range(0, len(lista) - i - 1):
            counter += 1
            if lista[a] > lista[a + 1]:
                lista[a + 1], lista[a] = lista[a], lista[a + 1]
    return [lista, counter]


if __name__ == '__main__':
    lista1 = [1, 23, 42, 63, 4, 16, 8, 94, 72, 45, 6]
    lista2 = [1, 23, 42, 63, 4, 16, 8, 94, 72, 45, 6]
    print(bubblesort(lista1))
    print(optimizedBsort(lista2)[0])
