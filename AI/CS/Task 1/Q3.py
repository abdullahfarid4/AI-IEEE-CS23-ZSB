dict1 = {
    "A": [20, 30, 100, 49],
    "B": [00, 199, 201, 29],
    "C": [40, 90, 69, 18]
}
temp = 0
temp1 = ''

for i in dict1:
    y = max(dict1[i])
    z = min(dict1[i])
    if (y - z) > temp:
        temp = y - z
        temp1 = i

print(temp1)
