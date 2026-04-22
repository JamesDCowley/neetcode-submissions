class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        base = {}
        for st in strs:
            sort_st = str(sorted(st))
            if sort_st in base:
                base[sort_st].append(st)
            else:
                base[sort_st] = [st]
        return base.values()