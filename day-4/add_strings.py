import sys
sys.set_int_max_str_digits(10000)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        total = int(num1) + int(num2)

        return f"{total}"

if __name__ == "__main__":

    num1 = input("Enter the number: ")

    num2 = input("Enter the number: ")

    sol = Solution()

    result = sol.addStrings(num1,num2)

    print(result)
