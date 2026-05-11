class Solution:

    def encode(self, strs: List[str]) -> str:
        acc = []
        for s in strs:
            acc.append(str(len(s)))
            acc.append("#")
            acc.append(s)
        return "".join(acc)

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []
        while i < len(s):

            digits = 0
            while s[i+digits] != "#":
                digits +=1
            
            str_len = int(s[i:i+digits])
            word_start = i + digits + 1
            word_end = word_start + str_len
            res.append(s[word_start:word_end])
            i = word_end
        return res