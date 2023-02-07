lst = list(map(int, input().split()))
lst2 = []

for i in lst:
    n_lst = lambda i: i % 2 == 0
    lst2.append(n_lst(i))

print(lst2.count(True))
