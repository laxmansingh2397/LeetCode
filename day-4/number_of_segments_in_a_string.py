
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


if __name__ == "__main__":

    s = input("Enter a string: ")

    sol = Solution()

    result = sol.countSegments(s)

    print(result)