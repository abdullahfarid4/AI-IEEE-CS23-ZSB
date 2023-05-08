import numpy as np

n = int(input("Enter an integer: "))

arr = np.arange(1, n+1)
arr2 = arr.copy()

for i in range(n - 1):
    arr2 = np.append(arr2, arr)

print(arr2.reshape(n, n))

