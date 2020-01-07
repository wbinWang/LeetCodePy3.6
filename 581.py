# 581 最短连续无序子数组

class Solution1:
    # 时间复杂度太高，超时
    def findUnsortedSubarray(self, nums: [int]) -> int:
        nums_len = len(nums)
        if nums_len < 2:
            return 0
        left = self.findLeft(nums)
        # print("left",left)
        if left == None:
            return 0
        right = self.findRight(nums)
        # print("right",right)
        if right == None:
            return 0
        
        return right - left + 1

    # 从左找到最小的
    def findLeft(self, nums: [int]) -> int:
        nums_len = len(nums)
        for i in range(0,nums_len - 1):
            n = nums[i]
            # 判断n是否为最小的
            for j in range(i + 1, nums_len):
                n1 = nums[j]
                if n > n1:
                    return i
    # 从右找到最大
    def findRight(self, nums: [int]) -> int:
        nums_len = len(nums)
        for i in range(0,nums_len - 1):
            n = nums[nums_len - 1 - i]
            # print("--",n)
            # 判断n是否为最小的
            for j in range(i + 1, nums_len):
                n1 = nums[nums_len - 1 - j]
                # print("-- --",n1)
                if n < n1:
                    return nums_len - 1 - i

class Solution:
    # 系统排序后，一一比对
    def findUnsortedSubarray(self, nums: [int]) -> int:
        nums_len = len(nums)
        if nums_len < 2:
            return 0
        nums1 = list(nums)
        nums1.sort()
        # print(nums)
        # print(nums1)
        left = None
        right = None
        for i in range(0, nums_len):
            if left == None:
                if nums[i] != nums1[i]:
                    left = i
            if right == None:
                j = nums_len - 1 - i
                if nums[j] != nums1[j]:
                    right = j
            if right != None and left != None:
                return right - left + 1              
        return 0


if __name__ == "__main__":
    # arr = [2, 6, 4, 8, 10, 9, 15]
    # arr = [1,2,4,5]
    arr = [1,2,3,5,4]
    print(Solution().findUnsortedSubarray(arr))