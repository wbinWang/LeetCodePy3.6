#  283 移动零

class Solution:
    # 自己的方法，在pop时操作太多了
    def moveZeroes1(self, nums) -> None:
        zero_count = 0
        i = 0
        while i < len(nums):
            n = nums[i]
            if n == 0:
                nums.pop(i)
                zero_count += 1
            else:
                i += 1
        while zero_count > 0:
            nums.append(0)
            zero_count -= 1

    # 看官方讲解，有感而发
    def moveZeroes(self, nums) -> None:
        no_zero_count = 0
        for i in range(0, len(nums)):
            n = nums[i]
            if n != 0:
                if no_zero_count != i:
                    nums[no_zero_count] = n
                    nums[i] = 0
                no_zero_count += 1


if __name__ == "__main__":
    nums = [0,2,1]
    print("1",nums)
    s = Solution()
    s.moveZeroes(nums)
    print("2",nums)