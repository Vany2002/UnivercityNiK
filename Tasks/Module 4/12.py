m = int(input())
d = int(input())
if (d == 31) and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10):
    m = m + 1
    d = d - 30
    print(f"{d}-{m}-2022")
elif (d > 0) and (d < 31) and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
    print(f"{d + 1}-{m}-2022")
elif d == 31 and m == 12:
    m = m - 11
    d = d - 30
    print(f"{d}-{m}-2023")
elif d == 28 and m == 2:
    m = m + 1
    d = d - 27
    print(f"{d}-{m}-2022")
elif (d > 0) and (d < 28) and m == 2:
    print(f"{d + 1}-{m}-2022")
elif (d == 30) and (m == 4 or m == 6 or m == 9 or m == 11):
    m = m + 1
    d = d - 29
    print(f"{d}-{m}-2022")
elif (d > 0) and (d < 30) and (m == 4 or m == 6 or m == 9 or m == 11):
    print(f"{d + 1}-{m}-2022")


