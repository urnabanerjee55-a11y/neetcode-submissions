class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) # {sorted word : original word anagrams}
        for word in strs :
            sortedword = "".join(sorted(word))
            hashmap[sortedword].append(word)
        return list(hashmap.values())