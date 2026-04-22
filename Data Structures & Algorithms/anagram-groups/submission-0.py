class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        baseAnagrams = {}

        for s in strs:
            base = str(sorted(s))
            if base in baseAnagrams:
                baseAnagrams[base].append(s)
            else:
                baseAnagrams[base] = [s]
        return baseAnagrams.values()