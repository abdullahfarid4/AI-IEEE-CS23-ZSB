def mean(lst: list):
    """
    :param lst:
    :return: mean/average of list
    """
    return sum(lst) / len(lst)


def median(lst: list):
    """
    :param lst:
    :return: median of list doesn't get affected by outliers
    """
    lst = sorted(lst)
    x = int(len(lst) / 2)
    if len(lst) % 2 == 0:
        return (lst[x] + lst[x - 1]) / 2
    else:
        return lst[x]


def mode(lst: list):
    temp_dict = {}
    repetitions_lst = []
    no_mode_flag = False
    mode_lst = []

    for i in list(set(lst)):
        repetitions = lst.count(i)
        temp_dict[i] = repetitions
        repetitions_lst.append(repetitions)

    temp_lst = set(repetitions_lst)

    if len(temp_lst) < 2:
        no_mode_flag = True
    else:
        for i in list(temp_dict.keys()):
            if temp_dict[i] == max(temp_lst):
                mode_lst.append(i)

    if not no_mode_flag:
        return mode_lst
    else:
        return "There is No Mode"


if __name__ == "__main__":

    while True:
        try:
            lst_input = list(map(float, input().split()))
            break
        except ValueError:
            print("Please enter a list of numbers")

    try:
        # An empty list will cause len(lst) = 0 which will cause a zero division
        print("Mean is:", "%.3f" % (mean(lst_input)))

        # An empty list will cause len(lst) of zero which will lead to an index error
        print("Median is:", median(lst_input))

        # An empty list will give max() an empty argument which leads to value error
        print("Mode is/are:", mode(lst_input))

    except (ValueError, IndexError, ZeroDivisionError):
        print("You have entered an empty list")
