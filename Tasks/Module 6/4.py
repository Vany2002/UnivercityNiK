lst = [int(s) for s in input().split()]
min, max = min(lst), max(lst)
mini, maxi = lst.index(min), lst.index(max)
lst[mini], lst[maxi] = lst[maxi], lst[mini]
print(*lst)