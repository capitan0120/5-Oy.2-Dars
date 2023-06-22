from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = list(set(letters))
        letters.sort()
        for i in letters:
            if i > target:
                return i
                break
        return letters[0]