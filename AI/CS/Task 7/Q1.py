from math import ceil

# While experimenting with the coin flipping, I noticed as the number of coin flips increased it started to take
# a shape of (x + 1)^n where n = 1, 2, 3,...etc which is called a pascal triangle
# 1 and 1 on the edges represent the extreme case of all heads or all tails
# and the rest of the numbers represent the number of occurrence of each non-extreme case


def create_pascal_triangle(num: int):
    """
    :param num:
    :return: pascal triangle
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1
    """
    lst2 = []
    temp = 1
    for j in range(1, num + 1):
        lst2.append(temp)
        temp = temp * (num - j) // j

    return lst2


ans = 0

flip_num = int(input("The number of flips: "))
h_or_t = input("Head or Tail? ").lower()

if h_or_t not in ['head', 'tail']:
    print("** sigh **")
    print("A coin doesn't have", h_or_t, "on it!")
    print("I am not mad; I am just disappointed")
    exit()

st = "The number of " + h_or_t + " appearance: "
h_or_t_app = int(input(st))

if h_or_t_app > flip_num:
    print("Please Enter a valid head/tail appearance")
    exit()

st2 = "The probability of " + h_or_t + "(< 1): "
h_or_t_prob = float(input(st2))

lst = create_pascal_triangle(flip_num + 1)

# Case of Fair Coin
if h_or_t_prob == 0.5:

    if h_or_t_app == flip_num:
        ans = 1 / 2**flip_num

    else:
        ans = lst[h_or_t_app] / 2**flip_num

# Case of Loaded Coin
else:

    if h_or_t_app == flip_num:
        ans = h_or_t_prob ** h_or_t_app

    else:
        ans = (h_or_t_prob ** h_or_t_app) * ((1 - h_or_t_prob) ** (flip_num - h_or_t_app))
        ans *= lst[h_or_t_app]


print("The answer is:", ceil(ans * 1000) / 1000.0)
