from random import randint
x = int(input("Введите максимальное кол-во спичек за ход: "))
while x<3:
    x = int(input("Минимальное число 3, повторите ввод: "))
i = int(input("число спичек в игре: "))
while i < ((x*5)-1):
    i = int(input("Минимальное число "+str((x*5)-1)+", повторите ввод: "))
n=0
if i % (x+1) == 0:
    t = 1
else:
    t = 0
#t = randint(0,1)
while i > 1:
    if t == 0:
        print("")
        print("")
        print("")
        n = int(input("выберите число 1 - " + str(x) +": "))
        while n < 1 or n > x:
            n = int(input("выберите число 1 - " + str(x) +": "))
        t = 1
        i = i - n
        print("")
        print("")
        print("")
        print("===========================")
        print("ваш ход: " + str(n))
        print("осталось: " + str(i))
        print("===========================")
        print("")
    else:
        if i > 1:
            if (i-1) % (x+1) == 0:
                n = randint(1,x)
            else: 
                ii = i
                while ii % (x+1) != 0:
                    ii = ii + 1
                n = x-(ii-i)
            t = 0
            i = i - n
            print("---------------------------")
            print("ход компьютера: " + str(n))
            print("осталось: " + str(i))
            print("---------------------------")
if t == 1:
    print("ты победил")
else:
    print('ты проиграл')

aaa=input("")
