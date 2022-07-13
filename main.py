import random

minDiapazon = 10
maxDiapazon = 100
count = 0
miss = 0
lives = 3


def start():
    print("""********************* Приветствую тебя в захватывающем мире математики! *********************
    
В этой игре ты столкнешься с невероятными математическми операциями. Будь осторожен ибо математика коварна и опасна!
Но ты всегда можешь остановиться введя слово 'СТОП'
Тебе будет задано 10 примеров. За каждую ошибку ты теряешь одну жизнь. Постарайся дойти до конца!
""")
    print()


def stop():
    print(f"""Игра закончена... 
Всего было примеров - {count}
Правильных ответов - {count-miss}""")


def checkresult(result, z):
    global miss, lives
    if result != z:
        miss += 1
        lives -= 1
        print(f"Неверно ! Правильный ответ {z}")
        print(f"Осталось жизней: {lives}\n")
    else:
        print("Верно!\n")


def funcsum():
    result = ""
    z = random.randint(minDiapazon, maxDiapazon)
    x = random.randint(minDiapazon, z)
    y = z - x

    if random.randint(0, 1):
        while not result.isdigit():
            result = input(f"{x} + {y} = ")
            if not result.isdigit():
                print("Введите число!")
    else:
        while not result.isdigit():
            result = input(f"{y} + {x} = ")
            if not result.isdigit():
                print("Введите число!")
    checkresult(int(result), z)


def funcSubtraction():
    result = ""
    x = random.randint(minDiapazon + 15, maxDiapazon - 15)
    y = random.randint(minDiapazon, maxDiapazon)
    z = abs(x - y)
    while not result.isdigit():
        result = input(f"{max(x,y)} - {min(x,y)} = ")
        if not result.isdigit():
            print("Введите число!")
    checkresult(int(result), z)



def funcMultiplication():
    result = ""
    x = random.randint(minDiapazon, maxDiapazon) // 5 + 1
    y = random.randint(minDiapazon, maxDiapazon) // x
    z = x * y
    if random.randint(0, 1):
        while not result.isdigit():
            result = input(f"{x} * {y} = ")
            if not result.isdigit():
                print("Введите число!")
    else:
        while not result.isdigit():
            result = input(f"{y} * {x} = ")
            if not result.isdigit():
                print("Введите число!")
    checkresult(int(result), z)
def funcDivision():
    result = ""
    x = random.randint(minDiapazon, maxDiapazon) // 10 + 1
    y = random.randint(minDiapazon, maxDiapazon) // x
    x = x * y
    z = x // y
    while not result.isdigit():
        result = input(f"{x} / {y} = ")
        if not result.isdigit():
            print("Введите число!")
    checkresult(int(result), z)

def main():
    global count

    start()
    while lives:
        count += 1
        func = random.randint(0, 4)
        if func == 0:
            funcsum()
        elif func == 1:
            funcSubtraction()
        elif func == 2:
            funcMultiplication()
        elif func == 3:
            funcDivision()
    stop()


if __name__ == '__main__':
    main()
