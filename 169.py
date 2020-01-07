# 169 多数元素
class Solution:
    # 哈希表的做法，速度有点慢
    def majorityElement2(self, nums) -> int:
        d = {}
        l = len(nums)
        for i in range(0, l):
            n = nums[i]
            if n in d:
                d[n] = d[n] + 1
            else:
                d[n] = 1
            if d[n] > l / 2:
                return n

    # 排序法 快！
    def majorityElement3(self, nums) -> int:
        nums.sort()
        return nums[int(len(nums) / 2)]

    
    # 使用自己写的排序法，自己写的quicksort很差，不知道是否为代码问题。python应用的是timsort
    def majorityElement(self, nums) -> int:
        nums = self.quickSort(nums)
        print(nums)
        return nums[int(len(nums) / 2)]

    # 快速排序
    def quickSort(self, nums) -> list:
        l = len(nums)
        if l < 2:
            return nums
        pivot = nums[0]
        left = []
        right = []
        for i in range(1,l):
            n = nums[i]
            if n <= pivot:
                left.append(n)
            else:
                right.append(n)
        return self.quickSort(left) + [pivot] + self.quickSort(right)



if __name__ == "__main__":
    arr = [1,1,2]
    print(Solution().majorityElement(arr))