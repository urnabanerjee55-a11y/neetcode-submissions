class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortednums = sorted(enumerate(nums),key=lambda x:x[1])
        i=0
        j=len(nums)-1
        for x in range(len(nums)):
            sum = sortednums[i][1]+sortednums[j][1]
            if sum==target:
                if sortednums[i][0]<sortednums[j][0]:
                    return [sortednums[i][0],sortednums[j][0]]
                else :
                    return [sortednums[j][0],sortednums[i][0]]    
            elif sum<target:
                i+=1
            else:
                j-=1        