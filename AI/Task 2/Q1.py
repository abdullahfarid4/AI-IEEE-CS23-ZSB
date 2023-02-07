def sortList(lst_temp: list):
    lst_temp = sorted(lst_temp)
    return lst_temp


def appearance(lst_temp: list, temp: int):
    try:
        first = lst_temp.index(temp)
        lst_temp = lst_temp[::-1]
        last = (len(lst_temp) - 1 ) - lst_temp.index(temp)
        return first, last
    except ValueError:
        return "The target is not in the list!"


lst = list(map(int, input().split()))
val = int(input())
lst = sortList(lst)
print(appearance(lst, val))
