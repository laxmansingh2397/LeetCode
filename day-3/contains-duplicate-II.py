from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False
    

if __name__ == "__main__":

    k = int(input("Enter the number you want to compare: "))

    nums = list(map(int, input().rstrip().split()))

    sol = Solution()

    result = sol.containsNearbyDuplicate(nums,k)

    print(result)
