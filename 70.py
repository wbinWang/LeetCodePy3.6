# 70 爬楼梯

class Solution:

    # 记忆递归法
    kv = {}
    def climbStairs(self, n: int) -> int:
        # print(n)
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if n not in self.kv:
                v = self.climbStairs(n - 1) + self.climbStairs(n - 2)
                self.kv[n] = v
                return v
            return self.kv[n]

    # 动态规划
    def climbStairs2(self, n: int) -> int:
        _kv = {1:1,2:2}
        for i in range(3,n + 1):
            _kv[i] = _kv[i - 1] + _kv[i - 2]
        return _kv[n]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs2(40))