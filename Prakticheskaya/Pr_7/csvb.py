import csv

def get_books(filename: str, name: str):
    with open(filename, 'r') as file:
        read = csv.reader(file, delimiter='|')
        res = [[]]
        res.clear()
        for row in read:
            if ''.join(row).__contains__(name):
                res.append(row)
        return res

def get_totals(data: [[]], usl = 500, dop = 100):
    res = [[]]
    res.clear()
    for row in data:
        count = int(row[3]) * float(row[4])
        if count < usl:
            count += dop
        res.append([row[0], count])
    return res

books = get_books("books.csv", "Python")
res = get_totals(books)

for i in res:
    print(i)
