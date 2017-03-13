def whiskey():
    print('i am daniel')

fw= open('sample.txt', 'w')
fw.write('first line of sample file\n')
fw.write('second line\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()


