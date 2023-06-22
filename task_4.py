from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        a = max(nums)
        nums.remove(a)
        for i in nums:
            print(i)
            if 2 * i > a:
                return -1
        return 1
obj = Solution()
print(obj.dominantIndex(nums=[3,6,1,0]))