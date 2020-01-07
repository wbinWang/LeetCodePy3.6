# 461 汉明距离
import math
class Solution:
    # 为啥没有这样解答的呢
    def hammingDistance2(self, x: int, y: int) -> int:
        ans = 0
        a = 32
        while a >= 0:
            aa = int(math.pow(2, a))
            x1 = int(x / aa)
            y1 = int(y / aa)
            if x1 != y1:
                ans += 1
            if x1 > 0:
                x = x % aa
            if y1 > 0:
                y = y % aa
            a -= 1
        return ans

    # 位操作
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        ans = 0
        while z > 0:
            if z & 1 == 1:
                ans += 1
            z = z >> 1
        return ans


if __name__ == "__main__":
    print(Solution().hammingDistance(1,4))