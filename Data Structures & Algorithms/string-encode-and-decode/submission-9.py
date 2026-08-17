class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for s in strs:
            n = len(s)
            res.append(str(n)+'#'+s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        print(s)
        if not s:
            return []
        res = []
        total = len(s)
        l = r = 0

        while r < total:
            while s[r] != '#':
                r = r + 1
            length = int(s[l:r])
            word = s[r+1:length+r+1]
            l = r = r + length+1
            res.append(word)

        return res
        
