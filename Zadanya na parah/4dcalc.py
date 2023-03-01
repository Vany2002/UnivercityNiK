import dcalc
from random import randint

def create_list(*args, **kwargs):
    c_list = []
    for i in range(len(args)):
        c_list.append(f"Point_{i} = {dcalc.gms(args[i])}")
    for name, value in kwargs.items():
        c_list.append(f"{name} = {dcalc.gms(value)}")
    return c_list

def get_coord():
    a = randint(1*100000, 360*100000)
    return a / 100000

print(create_list(get_coord(), get_coord(), get_coord(), get_coord(), pole=get_coord(), put_1=get_coord()))
