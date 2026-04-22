class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)

        if len(s1) > len(s2):
            return False
        occ = {}
        for ch in s1:
            if ch in occ:
                occ[ch] += 1
            else:
                occ[ch] = 1
        while r <= len(s2):
            sub = s2[l:r]
            occ2 = {}
            for ch in sub:
                if ch in occ2:
                    occ2[ch] += 1
                else:
                    occ2[ch] = 1
            print(occ)
            print(occ2)
            if occ == occ2:
                print("equal")
                print(occ)
                print(occ2)
                return True
            l += 1
            r += 1
        return False

