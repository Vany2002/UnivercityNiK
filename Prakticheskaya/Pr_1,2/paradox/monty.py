import random

def montyh(iter = 10000):
    nch = 0
    ch = 0
    for i in range(iter):
        a = [0, 0, 1]
        choice = random.randint(0, 2)
        a.pop(choice)
        a.remove(0)
        if a[0] == 1:
            nch += 1
        else:
            ch += 1
    return(f'Вероятность если поменять выбор: {nch / 100}%\nВероятность если не менять выбор: {ch / 100}%')