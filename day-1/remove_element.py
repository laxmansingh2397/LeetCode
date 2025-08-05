from typing import List

class Solution:
    def removeElement(self, nums: List[int], val:int) -> int:

        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k
    

if __name__ == "__main__":

    val = int(input("Enter a number to compare: "))

    nums = list(map(int, input().rstrip().split()))

    sol = Solution()

    result = sol.removeElement(nums,val)

    print(result, nums[ :result])