class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occ_map = {}

        for ch in s:
            if ch in occ_map:
                occ_map[ch] += 1
            else:
                occ_map[ch] = 1
        
        for ch in t:
            if ch in occ_map:
                occ_map[ch] -= 1
                if occ_map[ch] < 0:
                    return False
            else:
                return False

        for vals in occ_map.values():
            if vals != 0:
                return False
        return True
            