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

def toNull(s1, s2):

    start = time.time()

    s3 = list()
    counter = 0
    outcome = True
    for a in s1:
        counter += 1
        if a in s2:
            s3.append(None)
        else:
            s3.append(a)

    for index in s3:
        counter += 1
        if index is not None:
            outcome = False
            break

    end = time.time()
    duration = end-start

    return f'As strings {s1} e {s2} podem ser transpostas? {outcome}. Foram necessários {counter} passos e demorou {duration} segundos.'


# 2) Ordene os caracteres das duas strings. Se o resultado
# da ordenação forem duas strings iguais, então as
# strings são transponíveis. Conte o número de passos
# necessários e o tempo até obter a solução

def __orderString__(s1, s2):

    start = time.time()
    s3 = list()
    counter = 0

    for a in s2:
        counter += 1
        if a in s1:
            s3.append(a)
        else:
            s3.append("")

    s4 = "".join(s3)

    for index in s4:
        counter += 1
        if index is not None:
            outcome = False
            break

    end = time.time()
    duration = end-start

    return f'As strings {s1} e {s2} podem ser transpostas? {outcome}. Foram necessários {counter} passos e demorou {duration} segundos.'


# 3) Programe a variante “força bruta”, isto é, que testa todas as possibilidades. Para isso considere
# as letras da primeira string e faça uma lista com strings correspondentes a todas as combinações
# possíveis com essas letras. Finalmente, verifique se a segunda string se encontra na lista. Conte
# o número de passos necessários e o tempo até obter a solução.


def __permutations__(s1, s2):
    final_list = [[]]
    length = len(s1)
    groups = [list(s1)] * length
    print(groups)

    for j in groups:
        final_list = [x + [y] for x in final_list for y in j]

    permutations = [''.join(item) for item in final_list]

    return permutations.__contains__(s2)

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

    strs1 = __lettersCount__(s1)
    strs2 = __lettersCount__(s2)

    cnt1 = letcnt.countLetters(strs1, s1)
    cnt2 = letcnt.countLetters(strs2, s2)

    print(cnt1)
    print(cnt2)

    for k in cnt1:
        if k not in cnt2 or cnt1[k] != cnt2[k]:
            return False;

    return True;

# 5) Qual destas variantes executa menos passos até à solução? E qual é a mais rápida?



if __name__ == '__main__':

    print('1) ' + toNull("amror", "ramon"))
    #print('2) ' + __orderString__("promar", "ramorp"))
    #print('3) ' + __permutations__("promar", "ramorp"))
    #print('4) ' + __stringCounter__("romat","amror"))





