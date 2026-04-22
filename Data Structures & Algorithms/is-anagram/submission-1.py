class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occurences = {}

        for ch in s:
            if ch in occurences:
                occurences[ch] += 1
            else:
                occurences[ch] = 1
        
        for ch in t:
            if ch in occurences:
                if occurences[ch] == 0:
                    return False
                occurences[ch] -= 1
            else:
                return False

        return True
