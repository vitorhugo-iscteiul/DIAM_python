# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

file = open('poema.txt', 'r', encoding='utf-8')
poem = file.read()
vogais = ['a', 'e', 'i', 'o', 'u']
if __name__ == '__main__':
    count = 0
    for x in range(len(poem)):
        if poem[x] in vogais:
            count += 1

    print(count)
