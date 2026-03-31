class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()        
        left = 0
        right = len(nums) - 1
        count = 0       
        while left < right:
            current_sum = nums[left] + nums[right]           
            if current_sum == k:
                count = count + 1
                left = left + 1
                right = right - 1
            elif current_sum < k:
                left = left + 1
            else:
                right = right - 1               
        return count
