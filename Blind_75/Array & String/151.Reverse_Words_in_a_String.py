class Solution(object):
    def reverseWords(self, s:str) -> str:
        """
        :type s: str
        :rtype: str
        """

        return " ".join(s.split()[::-1])


if __name__ == "__main__":
    string = input()
    solution = Solution()
    print(solution.reverseWords(string))
