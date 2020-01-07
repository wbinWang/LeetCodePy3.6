# 448 找到数组中消失的数字

class Solution:
    # 哈希表
    def findDisappearedNumbers2(self, nums:[int]) -> [int]:
        if len(nums) == 0:
            return []
        d = {}
        for n in nums:
            if n not in d:
                d[n] = "1"
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in d:
                ans.append(i)
        return ans

    # 原地修改，太牛逼了！
    def findDisappearedNumbers(self, nums:[int]) -> [int]:
        if len(nums) == 0:
            return []
        for n in nums:
            x = nums[abs(n) - 1]
            if x > 0:
                nums[abs(n) - 1] = x * -1
        ans = []
        for i in range(0, len(nums)):
            n = nums[i]
            if n > 0:
                ans.append(i + 1)
        
        return ans


if __name__ == "__main__":
    arr = [4,3,2,7,8,2,3,1]
    # arr = [2,2,3,4]
    print(Solution().findDisappearedNumbers(arr))