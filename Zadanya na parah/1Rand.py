import random
Li = 3
b = 0

while True:
    r1 = random.randint(0, 500)
    r2 = random.randint(0, 500)
    r = r1 + r2
    answer = input(f"{r1} + {r2} = ? ")
    if not answer.isdigit():
        print("Введите число!")
        continue
    answer = int(answer)
    if answer == r:
        b += 1
    else:
        Li -= 1
        if Li == 0:
            print(f"Игра окончена! Вы набрали {b} очков!")
            break
        else:
            print(f"Неправильно! Осталось {Li} попытки")
