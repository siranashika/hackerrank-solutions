class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == target:
                    return curSum
                
                if abs(curSum - target) < abs(res - target):
                    res = curSum
                
                if curSum < target:
                    l += 1
                else:
                    r -= 1
        return res
