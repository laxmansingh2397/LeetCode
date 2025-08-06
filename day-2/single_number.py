from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0

        for num in nums:
            ans ^= num
        return ans
            

if __name__ == "__main__":

    nums = list(map(int, input().rstrip().split()))

    sol = Solution()

    result = sol.singleNumber(nums)

    print(result)