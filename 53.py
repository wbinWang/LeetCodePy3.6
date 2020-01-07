# 53 最大子序合

class Solution:

    # 动态规划
    def maxSubArray(self, nums: list) -> int:
        max_sum = nums[0]
        # 加分系数
        num = 0
        for i in nums:
            if num <= 0:
                num = i
            else:
                num = num + i
            max_sum = max(max_sum, num)
        return max_sum


    # 贪心算法
    # 每一步都是最佳方案，得到就是最优解？？？
    def maxSubArray3(self, nums: list) -> int:
        curr_sum = max_sum = nums[0]
        for i in range(1,len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum

    # 第一种方法
    def maxSubArray1(self, nums: list) -> int:
        while True:
            print(nums)
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            f1 = nums[0]
            e1 = nums[-1]
            if f1 <= 0 and e1 <= 0:
                if f1 < e1:
                    nums = nums[1:]
                else:
                    nums = nums[0:-1]
            elif f1 <= 0:
                nums = nums[1:]
            elif e1 <= 0:
                nums = nums[0:-1]
            else:
                f = nums[0] + nums[1]
                e = nums[-1] + nums[-2]
                if f > nums[0]:
                    nums = [f] + nums[2:]
                elif e > nums[-1]:
                    nums = nums[0:-2] + [e]
                else:
                    if f1 < e1:
                        nums = [f] + nums[2:]
                    else:
                        nums = nums[0:-2] + [e]

    # 第一种方法的优化
    def maxSubArray2(self, nums: list) -> int:
        while True:
            print(nums)
            num_len = len(nums)
            if num_len == 0:
                return 0
            if num_len == 1:
                return nums[0]
            f1 = nums[0]
            e1 = nums[-1]
            
            i1 = 1
            i2 = num_len
            if f1 < e1:
                i1 = 0
                i2 = num_len - 1

            if f1 <= 0 and e1 <= 0:
                nums = nums[i1:i2]
            elif f1 <= 0:
                nums = nums[1:]
            elif e1 <= 0:
                nums = nums[0:-1]
            else:
                f = nums[0] + nums[1]
                e = nums[-1] + nums[-2]
                if f > nums[0]:
                    nums = [f] + nums[2:]
                elif e > nums[-1]:
                    nums = nums[0:-2] + [e]
                else:
                    if f1 < e1:
                        nums = [f] + nums[2:]
                    else:
                        nums = nums[0:-2] + [e]

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4,-1]
    # arr = [-1,-2]
    # arr = [31,-41,59,26,-53,58,97,-93,-23,84]
    # arr = [1,-2,0]
    # arr = [3,-2,-3,-3,1,3,0]
    # arr = [-2,1,-3,4,-1,2,1,-5,4]
    # arr = [3,-2,-3,-3,1,3,0]
    # arr = [-3,1,0,-1,-2,3,2,-1]
    s = Solution()
    x = s.maxSubArray(arr)
    print(x)