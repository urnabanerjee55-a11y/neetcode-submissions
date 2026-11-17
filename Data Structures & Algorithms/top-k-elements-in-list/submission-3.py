class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        freqlist = [[] for i in range(len(nums)+1)]
        res = []
        for num in nums:
            freqmap[num] = 1 + freqmap.get(num,0)
        for num,f in freqmap.items() :
            freqlist[f].append(num)
        for i in range(len(freqlist) -1,0,-1) :
            for j in range(len(freqlist[i])) :
                res.append(freqlist[i][j])
                if len(res)==k:
                    return res


