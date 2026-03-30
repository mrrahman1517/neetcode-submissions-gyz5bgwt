class Solution:
    def climbStairs(self, n: int) -> int:
        #f = [0]*(n + 1)
        fp = 1
        fc = 1
        for i in range(2, n + 1):
            fs = fp + fc
            fp = fc
            fc = fs
            #f[i] = f[i-1] + f[i-2]
        return fc
        