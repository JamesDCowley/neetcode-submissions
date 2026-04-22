class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += str(len(st)) + "#" + st
        return s

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            str_len = int(s[i:j])
            i = j + 1
            j = i + str_len
            lst.append(s[i:j])
            i = j
        return lst
            
            
