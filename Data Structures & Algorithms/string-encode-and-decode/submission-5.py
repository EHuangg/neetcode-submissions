class Solution:

    def encode(self, strs: List[str]) -> str:
        # [Hello,world] -->  %5%Hello%5%world
        res = ""
        for s in strs:
            length = len(s)
            res += '%' + str(length) + '%' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            # processing word length
            if s[i] == '%':
                i += 1
                length = ""
                # integer
                while s[i] != '%':
                    length += s[i]
                    i += 1
                length = int(length)
            # processing word
            word = ""
            for j in range(i + 1, i + length + 1):
                word += s[j]
            i += length + 1
            res.append(word)

        return res


                
