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
    #s3 = ''.join(sorted(s1))
    #s4 = ''.join(sorted(s2))

    exe3.optimizedBsort(s3)
    exe3.optimizedBsort(s4)

    print(s3)
    print(s4)
    end = time.time()
    duration = end-start

    outcome = True
    for n in s3:
        if n not in s4 or n != s4[s4.index(n)]:
            outcome = False

    print(f'As strings {s1} e {s2} podem ser transpostas? {outcome}. Foram necessários {counter} passos e demorou {duration} segundos.')

    return [counter, duration]


# 3) Programe a variante “força bruta”, isto é, que testa todas as possibilidades. Para isso considere
# as letras da primeira string e faça uma lista com strings correspondentes a todas as combinações
# possíveis com essas letras. Finalmente, verifique se a segunda string se encontra na lista. Conte
# o número de passos necessários e o tempo até obter a solução.

final_list = []

def __allPermutations__(s1, s2):
    start = time.time()

    counter = 0
    outcome = False
    n = len(s1)

    __permutations__(s1, "", n)
    print(final_list)

    for item in final_list:
        counter += 1
        if "".join(item) == s2:
            outcome = True
            break

    end = time.time()
    duration = end - start

    print(f'As strings {s1} e {s2} podem ser transpostas? {outcome}. Foram necessários {counter} passos e demorou {duration} segundos.')
    return [counter, duration]

def __permutations__(s1, prefix, n):

    if n == 0:
        if [prefix] not in final_list:
            final_list.append([prefix])
        return

    for i in range(n):
        new_prefix = prefix + s1[i]
        __permutations__(s1, new_prefix, n - 1)

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

    strs1 = __lettersCount__(s1)
    counter += len(s1)
    strs2 = __lettersCount__(s2)
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
            outcome = False;

    end = time.time()
    duration = end - start

    print(f'As strings {s1} e {s2} podem ser transpostas? {outcome}. Foram necessários {counter} passos e demorou {duration} segundos.')
    return [counter, duration]

# 5) Qual destas variantes executa menos passos até à solução? E qual é a mais rápida?

if __name__ == '__main__':

    print('1) ')
    exer4_1 = __toNull__("amoter", "ramote")

    print('2) ')
    exer4_2 = __orderString__("mala", "alma")

    print('3) ')
    exer4_3 = __allPermutations__("alme", "mala")

    print('4) ')
    exer4_4 = __stringCounter__("romat", "amror")

    passos = [exer4_1[0], exer4_2[0], exer4_3[0], exer4_4[0]]
    tempos = [exer4_1[1], exer4_2[1], exer4_3[1], exer4_4[1]]
    print(passos)
    print(tempos)

    winner_passos = [1, exer4_1[0]]
    winner_time = [1, exer4_1[1]]

    print(winner_passos)
    print(winner_time)

    for pas in range(0, 3):
        if passos[pas] < winner_passos[1]:
            winner_passos[0] = pas

    for tem in range(0, 3):
        if tempos[tem] < winner_time[1]:
            winner_time[1] = tem

    print(f' o vencedor em passos é o algoritmo {winner_passos[0]} e em tempo é o {winner_time[0]}')





