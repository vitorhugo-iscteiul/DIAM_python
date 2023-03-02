# 3.4 Estruturas de controlo
# Considere a operação de transposição de letras através da qual uma palavra ou uma frase pode ser
# composta com as letras de outra palavra ou de outra frase.
# Por exemplo, a palavra “amor” resulta da transposição de letras da palavra “roma”. Ou um outro
# exemplo, com mais de uma palavra:
# Conceba várias variantes de um programa que recebe duas strings e devolve True se as strings são
# transponíveis ou devolve False se as strings não são transponíveis. Considere que as duas strings têm
# igual número de caracteres alfabéticos. Todos os caracteres são minúsculos.
# As variantes para a transposição de letras são as seguintes:

# a) Verifique se cada caracter da primeira string existe também na segunda string. Se existir, retire
# o caracter na segunda string e substitua-o por “None”. Se no final do processo a segunda string
# for composta apenas por “None”, então as strings podem ser transpostas. Conte o número de
# passos necessários até obter a solução. Considere que um passo é uma iteração numa cadeia
# de caracteres. Conte também o tempo necessário até obter a solução.
def toNull(s1, s2):
    s3 = ""
    for a in s1:
        for b in s2:
            if b == a:
                s3 += s2.replace(b, "None")
                print(a, b)
    print(s3)


if __name__ == '__main__':
    toNull("roma", "amor")

# b) Ordene os caracteres das duas strings. Se o resultado da ordenação forem duas strings iguais,
# então as strings são transponíveis. Conte o número de passos necessários e o tempo até obter
# a solução.
# c) Programe a variante “força bruta”, isto é, que testa todas as possibilidades. Para isso considere
# as letras da primeira string e faça uma lista com strings correspondentes a todas as combinações
# possíveis com essas letras. Finalmente, verifique se a segunda string se encontra na lista. Conte
# o número de passos necessários e o tempo até obter a solução.
# d) Considere as duas strings. Conte o número de cada caractere que existe em cada string. Por
# exemplo, o número de “a” em cada string, o número de “b” em cada string, etc. Se o número
# de cada caractere em cada string for igual, então as duas strings são transponíveis. Conte o
# número de passos necessários e o tempo até obter a solução.
# e) Qual destas variantes executa menos passos até à solução? E qual é a mais rápida?
