a = int(input())
if a // 100 < a // 10 % 10 < a % 10:
    print("Да")
else:
    print("Нет")