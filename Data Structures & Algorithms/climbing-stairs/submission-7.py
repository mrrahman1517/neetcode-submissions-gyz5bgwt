class Solution:
    def climbStairs(self, n: int) -> int:
        fp = 1
        fc = 1
        for i in range(2, n + 1):
            fs = fp + fc
            fp = fc
            fc = fs
        return fc
        