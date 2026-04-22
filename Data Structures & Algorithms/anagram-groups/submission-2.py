class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            occ = [0] * 26
            for ch in s:
                occ[ord(ch) - 97] += 1
            res[tuple(occ)].append(s)
        return list(res.values())