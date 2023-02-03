lst = list(input().split())
lst1 = []
lst2 = []

for i in lst:
    x = len(i) / 2
    if len(i) % 2 != 0:
        x += 1
    lst1.append(i[:int(x)])
    lst2.append(i[int(x):])

print(lst1)
print(lst2)
