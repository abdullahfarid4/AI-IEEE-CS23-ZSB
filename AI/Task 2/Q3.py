def max_sum(lst_temp : list):
    lst_temp = sorted(lst_temp)
    large_sub = lst_temp[-2:]
    large = lst_temp[-1] + lst_temp[-2]
    for i in range(len(lst_temp) - 3, -1, -1):
        if lst_temp[i] + large > large:
            large = large + lst_temp[i]
            large_sub.append(lst_temp[i])
        else:
            break
    print('{} ({})'.format(large_sub, large))


def min_sum(lst_temp : list):
    lst_temp = sorted(lst_temp)
    small_sub = lst_temp[:2]
    small = lst_temp[0] + lst_temp[1]
    for i in range(2, len(lst_temp)):
        if lst_temp[i] + small < small:
            small = small + lst_temp[i]
            small_sub.append(lst_temp[i])
        else:
            break
    print('{} ({})'.format(small_sub, small))


lst = list(map(int, input().split()))
max_sum(lst)
min_sum(lst)
