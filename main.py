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


def funcsum():
    z = random.randint(minDiapazon,maxDiapazon)
    x = random.randint(minDiapazon, z)
    y = z - x

    if random.randint(0, 1):
        result = input(f"{x} + {y} = ")
    else:
        result = input(f"{y} + {x} = ")
    checkresult(result, z)


start()
for _ in range(3):
    count += 1
    z = funcsum()

stop()




