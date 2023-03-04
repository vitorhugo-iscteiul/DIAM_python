# 3.4 Estruturas de controlo
# Considere a operação de transposição de letras através da qual uma palavra ou uma frase pode ser
# composta com as letras de outra palavra ou de outra frase.
# Por exemplo, a palavra “amor” resulta da transposição de letras da palavra “roma”. Ou um outro
# exemplo, com mais de uma palavra:
# Conceba várias variantes de um programa que recebe duas strings e devolve True se as strings são
# transponíveis ou devolve False se as strings não são transponíveis. Considere que as duas strings têm
# igual número de caracteres alfabéticos. Todos os caracteres são minúsculos.
# As variantes para a transposição de letras são as seguintes:

# 1) Verifique se cada caracter da primeira string existe também na segunda string. Se existir, retire
# o caracter na segunda string e substitua-o por “None”. Se no final do processo a segunda string
# for composta apenas por “None”, então as strings podem ser transpostas. Conte o número de
# passos necessários até obter a solução. Considere que um passo é uma iteração numa cadeia
# de caracteres. Conte também o tempo necessário até obter a solução.

import time

def __toNull__(s1, s2):

    start = time.time()

    s4 = list(s2)
    counter = 0
    outcome = True

    for i in s1:
        counter += 1
        if i in s4:
            s4[s4.index(i)] = None
        else:
            outcome = False

    print(s4)

    end = time.time()
    duration = end-start

    print(f'As strings {s1} e {s2} podem ser transpostas? {outcome}. Foram necessários {counter} passos e demorou {duration} segundos.')
    return [counter, duration]

# 2) Ordene os caracteres das duas strings. Se o resultado
# da ordenação forem duas strings iguais, então as
# strings são transponíveis. Conte o número de passos
# necessários e o tempo até obter a solução

import exe3

def __orderString__(s1, s2):

    start = time.time()
    counter = 0

    s3 = list(s1)
    s4 = list(s2)

    s3_order = exe3.optimizedBsort(s3)
    s4_order = exe3.optimizedBsort(s4)

    counter += s3_order[1]
    counter += s4_order[1]

    outcome = True

    for i in range(len(s3_order[0])):
        counter += 1
        if s4[i] != s3[i]:
            outcome = False
            break

    print(s3)
    print(s4)

    end = time.time()
    duration = end - start

    print(
        f'As strings {s1} e {s2} podem ser transpostas? {outcome}. Foram necessários {counter} passos e demorou {duration} segundos.')
    return [counter, duration]

# 3) Programe a variante “força bruta”, isto é, que testa todas as possibilidades. Para isso considere
# as letras da primeira string e faça uma lista com strings correspondentes a todas as combinações
# possíveis com essas letras. Finalmente, verifique se a segunda string se encontra na lista. Conte
# o número de passos necessários e o tempo até obter a solução.

final_list = []
counter = [0]

def __allPermutations__(s1, s2):
    start = time.time()

    outcome = False
    __permutations__(list(s1))
    #print(final_list)

    for item in final_list:
        counter[0] += 1
        if "".join(item) == s2:
            outcome = True
            break

    end = time.time()
    duration = end - start

    print(
        f'As strings {s1} e {s2} podem ser transpostas? {outcome}. Foram necessários {counter} passos e demorou {duration} segundos.')
    return [counter[0], duration]


# Function to swap two characters in a character array
def __swap__(s1, i, j):
    temp = s1[i]
    s1[i] = s1[j]
    s1[j] = temp

def __permutations__(s1, n=0):
    if n == len(s1) - 1:
        final_list.append(["".join(s1)])

    for i in range(n, len(s1)):
        counter[0] += 1
        __swap__(s1, n, i)
        __permutations__(s1, n + 1)
        __swap__(s1, n, i)


# 4) Considere as duas strings. Conte o número de cada caractere que existe em cada string. Por
# exemplo, o número de “a” em cada string, o número de “b” em cada string, etc. Se o número
# de cada caractere em cada string for igual, então as duas strings são transponíveis. Conte o
# número de passos necessários e o tempo até obter a solução.

def __lettersCount__(s1):
    strs = ''
    for letr in s1:
        if letr not in strs:
            strs = strs + letr
    return strs

def __stringCounter__(s1,s2):

    import exe2 as letcnt

    start = time.time()

    counter = 0
    outcome = True

    strs1 = __lettersCount__(sorted(s1))
    counter += len(s1)
    strs2 = __lettersCount__(sorted(s2))
    counter += len(s2)

    cnt1 = letcnt.countLetters(strs1, s1)
    counter += len(s1)
    cnt2 = letcnt.countLetters(strs2, s2)
    counter += len(s2)

    print(cnt1)
    print(cnt2)

    for k in cnt1:
        counter += 1
        if k not in cnt2 or cnt1[k] != cnt2[k]:
            outcome = False

    end = time.time()
    duration = end - start

    print(
        f'As strings {s1} e {s2} podem ser transpostas? {outcome}. Foram necessários {counter} passos e demorou {duration} segundos.')
    return [counter, duration]

# 5) Qual destas variantes executa menos passos até à solução? E qual é a mais rápida?

if __name__ == '__main__':

    import random as rand
    import string

    # N = 10
    # res1 = ''.join(rand.choices(string.ascii_lowercase, k=N))
    # res2 = ''.join(rand.choices(string.ascii_lowercase, k=N))

    res1 = 'Antónia'
    res2 = 'cautini'

    print(' Exercicio 1)')
    exer4_1 = __toNull__(res1, res2)

    print('Exercicio  2)')
    exer4_2 = __orderString__(res1, res2)

    print('Exercicio  3)')
    exer4_3 = __allPermutations__(res1, res2)

    print('Exercicio  4)')
    exer4_4 = __stringCounter__(res1, res2)

    passos = [exer4_1[0], exer4_2[0], exer4_3[0], exer4_4[0]]
    tempos = [exer4_1[1], exer4_2[1], exer4_3[1], exer4_4[1]]

    print(passos)
    print(tempos)

    winner_passos = min(passos)
    winner_time = min(tempos)

    print(f' o vencedor em passos é o algoritmo {passos.index(winner_passos)+1} e em tempo é o algoritmo {tempos.index(winner_time)+1}')





