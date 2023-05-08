lst = list(map(int, input().split()))
rot = int(input())

if rot > len(lst):
    rot = rot % len(lst)

while rot != 0:
    x = lst.pop(-1)
    lst.insert(0, x)
    rot -= 1
    
print(lst)
