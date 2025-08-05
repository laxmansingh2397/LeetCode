from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        nums.append(target)
        nums.sort()

        return nums.index(target)
    

if __name__ == "__main__":

    nums = list(map(int, input().rstrip().split()))

    target = int(input("Enter the number: "))

    sol = Solution()

    result = sol.searchInsert(nums, target)

    print(result)