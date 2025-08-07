from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s

if __name__ == "__main__":

    s = list(map(int, input().rstrip().split()))

    sol = Solution()

    result = sol.reverseString(s)

    print(result)
    