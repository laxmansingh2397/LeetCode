from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
        
        return max_count

if __name__ == "__main__":

    nums = list(map(int, input().rstrip().split()))

    sol = Solution()

    result = sol.findMaxConsecutiveOnes(nums)

    print(result)
