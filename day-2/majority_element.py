from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        max_count = 0
        number = 0
        set_nums = set(nums)
        for num in set_nums:
            if nums.count(num) > max_count:
                number = num
                max_count = nums.count(num)
        return number
    
if __name__ == "__main__":

    nums = list(map(int, input().rstrip().split()))

    sol = Solution()

    result = sol.majorityElement(nums)

    print(result)