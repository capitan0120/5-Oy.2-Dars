from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ll = []
        for i in range(left, right + 1):
            d = True
            k = i
            while k:
                a = k % 10
                if(a == 0) or (i % a != 0):
                    d = False
                k //= 10
            if d:
                ll.append(i)
        return ll
obj = Solution()
print(obj.selfDividingNumbers(left=1, right=22))