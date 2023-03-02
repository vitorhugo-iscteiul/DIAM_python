# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def countLetters(letras, texto):
    count = {}.fromkeys(letras, 0)  # cria o hashmap

    for letras in texto:
        if letras in count:
            count[letras] += 1
    return count  # devolve o hashmap


a = 0


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
# poem = "aaeeiou"
poem.casefold()

if __name__ == '__main__':
    print(poem.count("a"))
    countLets(poem)
    # result = countLetters(vogais, poem)
    #
    # print("O numero de cada vogal no texto é: " + str(result))
    #
    # maxi = max(result.values())
    # result2 = ([k for k in result if result.get(k) == maxi])
    # if len(result2) > 1:
    #     print("Há vários vencedores")
    #     print("os varios vencedores são: " + str(result2))
    # else:
    #     print("A vogal mais utilizada foi: '" + result2[0] + "'")
