class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle == "":
            return 0
        
        i = 0

        while i <= len(haystack) - len(needle):

            if haystack[i: i + len(needle)] == needle:
                return i
            i += 1

        return -1
    

if __name__ == "__main__":

    needle = input("Enter string to compare: ")

    haystack = input("Enter the string: ").strip()

    sol = Solution()

    result = sol.strStr(haystack,needle)

    print(result)
