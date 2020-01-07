# 121 买卖股票的最佳时机
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 1:
            return 0
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            curr = prices[i]
            if curr < buy:
                buy = curr
            else:
                profit = max(profit, curr - buy)

        return profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([8, 11, 1, 3, 0]))