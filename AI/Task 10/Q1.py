# Time Limit Exceeded :(
# 322 / 322 testcases passed

# Main Idea is to find the boundaries where the water could be trapped
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        i = 0
        lst1, lst2 = [], []

        if len(set(height)) > 1:
            while i < len(height) - 1:
                lst1 = height[:i+1]
                max1 = max(lst1)

                lst2 = height[i:]
                max2 = max(lst2)

                ans += min(max1, max2) - height[i]
                i += 1
            return ans
        else:
            return 0


