# 3.2 Exercício sobre strings e estruturas de controlo
# Considere novamente o início do poema “Corrente” de
# Chico Buarque.
# 1 - Escreva e execute um programa que:
# ! conta o número de vogais existentes no texto;
# ! imprime na consola as ocorrências da cada vogal;
# ! identifica a vogal mais utilizada;
# ! imprime na consola a vogal mais utilizada;
# ! se existirem várias vogais empatadas com o maior
# número de ocorrências, deve imprimir “Há vários
# vencedores.”.
# 2 - Melhore o seu programa de forma identificar quem
# são os vários vencedores em caso de empate.


def countLetters(letras, texto):
    count = {}.fromkeys(letras, 0)  # cria o hashmap

    for letras in texto:
        if letras in count:
            count[letras] += 1
    return count  # devolve o hashmap

#alternativamente

def countLets(texto):
    a = texto.count('a')
    e = texto.count('e')
    i = texto.count('i')
    o = texto.count('o')
    u = texto.count('u')
    resulte = " a: " + str(a) + " e: " + str(e) +" i: " + str(i) + " o: " + str(o) +" u: " + str(u)
    print(resulte)


vogais = 'aeiou'
file = open('poema.txt', 'r', encoding='utf-8')
poem = file.read()
poem.casefold()

if __name__ == '__main__':
    # print(poem.count("a"))
    # countLets(poem)

    result = countLetters(vogais, poem)
    #
    print("O número de ocorrências de cada vogal no texto é: " + str(result))
    #
    maxi = max(result.values())
    result2 = ([k for k in result if result.get(k) == maxi])
    if len(result2) > 1:
        print("Há vários vencedores")
        print("os varios vencedores são: " + str(result2))
    else:
        print("A vogal mais utilizada foi: '" + result2[0] + "'")
