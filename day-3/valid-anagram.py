class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_t = set(t)

        for i in set_t:
            if s.count(i) != t.count(i) or len(s) != len(t):
                return False
        return True

if __name__ == "__main__":

    s = input("Enter a string: ")

    t = input("Enter a string to compare: ")

    sol = Solution()

    result = sol.isAnagram(s,t)

    print(result)
