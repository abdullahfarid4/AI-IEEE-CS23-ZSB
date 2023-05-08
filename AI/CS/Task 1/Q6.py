dict1 = {}
temp = list(input().replace(':', ',').split(','))
temp2 = list(input().replace(':', ',').split(','))

for i in range(len(temp) - 1):
    if i % 2 != 0:
        continue
    dict1[temp[i]] = int(temp[i+1])

for i in range(len(temp2) - 1):
    if i % 2 != 0:
        continue
    dict1[temp2[i]] = int(temp2[i+1])

print(dict1)
