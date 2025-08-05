class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        list_s = s.split()

        return len(list_s[-1])


if __name__ == "__main__":

    s = input("Enter a string: ")

    sol = Solution()

    result = sol.lengthOfLastWord(s)

    print(result)