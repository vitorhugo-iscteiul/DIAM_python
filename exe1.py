# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

file = open('poema.txt', 'r', encoding='utf-8')

estrofe = ["Por isso eu fiz um samba bem pra frente","Dizendo realmente o que é que eu acho","Isso me deixa triste e cabisbaixo"]


def readfile():
    return file.read().split(' / ')

if __name__ == '__main__':

    poem = readfile()
    # 3.1 a)
    print("o 5º verso  é o: " + poem[4])
    print('O 6º verso é o : ' + poem[5])

    print("\n")

    # 3.1 b)
    for x in poem:
         print(x)

    # 3.1 c)
    poemafinal = poem + estrofe

    # 3.1 d)
    print(poemafinal[-2:])

    