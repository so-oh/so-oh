from random import randint 



RandomNumber = randint(1, 100)

while True:
    getNumber = int(input('1から100の間で数字を入れてください'))

    if(getNumber > RandomNumber):
        print('大きすぎます')
    elif(getNumber == RandomNumber):
        print('正解です！')
        break
    else:
        print('小さすぎます')

