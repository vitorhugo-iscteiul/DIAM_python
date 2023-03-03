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
import collections


def toNull(s1, s2):
    s3 = list()
    counter = 0
    for a in s2:
        counter += 1
        if a in s1:
            s3.append(None)
        else:
            s3.append(a)
    print(s3)
    print(counter)
    __validateResult__(s3)


def __validateResult__(list):
    for index in list:
        print(list.index(index))
        if index != None:
            print("False")
            return False;
    print("True")
    return True;


# 2) Ordene os caracteres das duas strings. Se o resultado
# da ordenação forem duas strings iguais, então as
# strings são transponíveis. Conte o número de passos
# necessários e o tempo até obter a solução

def __orderString__(s1, s2):
    print("s1:" + s1)
    print("s2:" + s2)
    s3 = list()
    counter = 0
    for a in s2:
        counter += 1
        if a in s1:
            s3.append(a)
        else:
            s3.append("")
    s1 = "".join(s3)
    print("s1:" + s1)
    print("s2:" + s2)
    print(counter)


# 3) Programe a variante “força bruta”, isto é, que testa todas as possibilidades. Para isso considere
# as letras da primeira string e faça uma lista com strings correspondentes a todas as combinações
# possíveis com essas letras. Finalmente, verifique se a segunda string se encontra na lista. Conte
# o número de passos necessários e o tempo até obter a solução.


def __permutations__(s1,s2):
    final_list = [[]]
    length = len(s1)
    groups = [list(s1)] * length

    for j in groups:
        final_list = [x + [y] for x in final_list for y in j]

    permutations = [''.join(item) for item in final_list]

    return permutations.__contains__(s2)

# 4) Considere as duas strings. Conte o número de cada caractere que existe em cada string. Por
# exemplo, o número de “a” em cada string, o número de “b” em cada string, etc. Se o número
# de cada caractere em cada string for igual, então as duas strings são transponíveis. Conte o
# número de passos necessários e o tempo até obter a solução.


# 5) Qual destas variantes executa menos passos até à solução? E qual é a mais rápida?


if __name__ == '__main__':
    # toNull("romar", "amror")
    # __orderString__("promar", "ramorp")
     print(__permutations__("promar", "ramorp"))



