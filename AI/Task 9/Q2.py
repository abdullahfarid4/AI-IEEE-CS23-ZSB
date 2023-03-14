# Accepted Answer
# Runtime: 32 ms
# Memory: 15.6 MB

# I am still learning regex but this was a good opportunity to practice on it
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :param s: string
        :return: True or False ( Palindrome or NOT )
        """
        # I am pretty sure that
        # there is a simpler way of doing these cases but have not figured them out yet
        s = s.replace('_', '').replace('[', '').replace(']', '').replace('`', '')

        reg = re.compile('[^0-9a-zA-z]')
        reg2 = reg.sub('', s).lower()
        if reg2 == reg2[::-1]:
            return True
        return False
