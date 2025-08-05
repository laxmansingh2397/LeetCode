from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        string_digits = "".join(str(i) for i in digits)
        plus_one_digits = str(int(string_digits) + 1)

        result = [int(digit) for digit in plus_one_digits]

        return result


if __name__ == "__main__":

    digits = list(map(int, input().rstrip().split()))

    sol = Solution()

    result = sol.plusOne(digits)

    print(result)