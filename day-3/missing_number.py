from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        This solution is for time complexity
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
        """
        if len(nums) == 1 and nums[0] != 0:
            return 0            

        for i in range(len(nums)+1):
            if i not in nums:
                return i
        

if __name__ == "__main__":

    nums = list(map(int, input().rstrip().split()))

    sol = Solution()

    result = sol.missingNumber(nums)

    print(result)