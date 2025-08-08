from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set =set(nums)
        output = []
        for i in range(1,len(nums)+1):
            if i not in num_set:
                output.append(i)

        return output

if __name__ == "__main__":

    nums = list(map(int, input().rstrip().split()))

    sol = Solution()

    result = sol.findDisappearedNumbers(nums)

    print(result)
      
