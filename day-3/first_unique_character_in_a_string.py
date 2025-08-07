class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for num in s:
            freq[num] = freq.get(num,0) + 1
        for i,num in enumerate(s):
            if freq[s[i]] == 1:
                return i
        return -1

if __name__ == "__main__":

    s = input("Enter a string: ")

    sol = Solution()

    result = sol.firstUniqChar(s)

    print(result)
