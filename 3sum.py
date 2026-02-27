from typing import list 
class solution:
    def threeSum(self,nums: list[int]) ->list[list[int]]:
        ans=[]
        size=len (nums)
        nums.sort()
        for x in range
        if( x>0 and nums (x)==nums[x-1])
         continue
        start=x+1
        end =size-1
        while start<end:
           sum=nums[x]+nums [start]+nums [end]
           if sum==0