import numpy as np

even_c = np.arange(2, 33, 2).reshape((4, 4))

print(even_c, '\n')

mn = np.mean(even_c)
stdn = np.std(even_c)

flag = even_c[:, :] <= (mn + 0.5 * stdn)
flag2 = even_c[:, :] >= (mn - 0.5 * stdn)

print(even_c[np.logical_and(flag, flag2)])
