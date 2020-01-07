# 136 只出现一次的数字
class Solution:

    # 既耗时、又费内存的办法
    def singleNumber2(self, nums) -> int:
        if len(nums) == 0:
            return 0
        d = []
        for i in nums:
            if i in d:
                d.remove(i)
            else:
                d.append(i)
        return d[0]

    # 只耗内存
    def singleNumber3(self, nums) -> int:
        if len(nums) == 0:
            return 0
        d = {}
        for i in nums:
            if i in d:
                del d[i]
            else:
                d[i] = 1
        return list(d.keys())[0]

    # 异或
    def singleNumber(self, nums) -> int:
        if len(nums) == 0:
            return 0
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        return ans
            

if __name__ == "__main__":
    print(Solution().singleNumber([10,9,9]))