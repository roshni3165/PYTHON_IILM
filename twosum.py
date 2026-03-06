class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in num_map:
                return [num_map[diff], i]
            
            num_map[nums[i]] = i