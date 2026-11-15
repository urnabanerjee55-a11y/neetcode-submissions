class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if (i!=j):
                    xsum = nums[i]+nums[j]
                    if (xsum==target):
                        return [i,j]
