from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n - 1]
            n = n - 1
            last = last - 1


        return nums1
    

if __name__ == "__main__":

    m = int(input("Enter the length of first array: "))
    
    nums1 = list(map(int, input().rstrip().split()))
    
    n = int(input("Enter the length of second array: "))

    nums2 = list(map(int, input().rstrip().split()))

    sol = Solution()

    result = sol.merge(nums1, m, nums2, n)

    print(result)