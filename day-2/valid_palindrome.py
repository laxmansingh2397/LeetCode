
class Solution:
    def isPalindrome(self, s: str) -> bool:
        compare = ""

        for char in s:
            if char.isalnum():
                compare += char.lower()

        return compare == compare[::-1]
    

if __name__ == "__main__":

    s = input("Enter a sting to compare: ")

    sol = Solution()

    result = sol.isPalindrome(s)

    print(result)
