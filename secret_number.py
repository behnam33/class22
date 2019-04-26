import random

secret1 = random.randint(0, 5)
i = 0

while i < 3:
    i = (i + 1)
    number = input("type number")
    number = int(number)
    if number< secret1:
        print( 'your number is low')
    elif number>secret1:
        print('your number is biger')

    else:
     print("bingo")
9