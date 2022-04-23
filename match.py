from random import randint
n=0
i=20
x=3
lvl=3
def Ai(i,x):
    if (i-1) % (x+1) == 0:
        n = randint(1,x)
    else: 
        ii = i
        while ii % (x+1) != 0:
            ii = ii + 1
        n = x-(ii-i)
    return n

t = randint(0,1)
while i > 1:
    if t == 0:
        n = int(input("выберите число 1 - " + str(x) +": "))
        while n < 1 or n > x:
            n = int(input("выберите число 1 - " + str(x) +": "))
        t = 1
        i = i - n
        print(i)
    else:
        if i > 1:
            n = Ai(i,x)
            if lvl == 1:
                if i > 8:
                    n = randint(1,x)
            if lvl == 2:
                if i > 14:
                    n = randint(1,x)      
            t = 0
            i = i - n
            print(i)
if t == 1:
    print("ты победил")
else:
    print('ты проиграл')

