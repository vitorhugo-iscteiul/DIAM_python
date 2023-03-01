# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def contaLetras(letras, texto):

    count = {}.fromkeys(letras, 0)

    for letras in texto:
        if letras in count:
            count[letras] += 1
    return count


vogais = 'aeiou'
file = open('poema.txt', 'r', encoding='utf-8')
poem = file.read()
poem.casefold()


if __name__ == '__main__':

    print(contaLetras(vogais, poem))
