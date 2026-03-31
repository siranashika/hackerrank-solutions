class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        pos = 0
        n = len(nums)       
        for i in range(n):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos = pos + 1     
        while pos < n:
            nums[pos] = 0
            pos = pos + 1
