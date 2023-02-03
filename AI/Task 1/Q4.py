lst = list(map(int, input().split()))
target = int(input())
flag = True

# Could have solve it using hashtable
# But Since it is only 2 values that make sum
# It is more difficult to implement

for i in range(len(lst)):
    if not flag:
        break
    for j in range(0, i):
        if lst[i] + lst[j] == target:
            print(j, ",", i)
            flag = False
