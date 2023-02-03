lst = list(map(int, input().split()))
if lst == lst[::-1]:
    print("Symmetric")
else:
    print("Not Symmetric")
