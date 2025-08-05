from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                

if __name__ == "__main__":

    target = int(input("Enter the target number: "))

    nums = list(map(int, input().rstrip().split()))

    sol = Solution()

    result = sol.twoSum(nums,target)
    print(result)

