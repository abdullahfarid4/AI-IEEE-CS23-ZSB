# Accepted Answer
# Runtime: 770 ms
# Memory: 15.8MB

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        """
        :param arr:
        :return lst: list with Elements with Greatest Element on Right Side
        """
        temp = len(arr)

        # Create a new zero list instead of an empty one to avoid using append
        lst = [0] * temp
        lst[-1] = -1

        if temp == 1:
            return lst

        # Started from the right to avoid the use of max() function
        while temp > 1:
            if arr[temp - 1] > lst[temp - 1]:
                lst[temp - 2] = arr[temp - 1]
            else:
                lst[temp - 2] = lst[temp - 1]
            temp -= 1

        return lst


# s = Solution()
# print(s.replaceElements([17, 18, 6]))
