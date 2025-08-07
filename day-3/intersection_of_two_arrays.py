from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        output = []

        for i in nums1:
            if i in nums2 and i not in  output:
                output.append(i)
        return output


if __name__ == "__main__":

    nums1 = list(map(int, input().rstrip().split()))

    nums2 = list(map(int, input().rstrip().split()))

    sol = Solution()

    result = sol.intersection(nums1, nums2)

    print(result)