class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        s = bin(n)[2:]
        return self.helper(s)

    def helper(self, s):
        while s and s[0] != "1":
            s = s[1:]
        if not s:
            return 0
        return (2 ** len(s) - 1) - self.helper(s[1:])
