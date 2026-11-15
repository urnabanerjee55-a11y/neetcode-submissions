class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssorted = sorted(list(s))
        tsorted = sorted(list(t))
        strssorted = str(ssorted)
        strtsorted = str(tsorted)
        if (strssorted==strtsorted) :
            return True
        else :
            return False    