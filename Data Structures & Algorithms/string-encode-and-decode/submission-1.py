class Solution:

    def encode(self, strs: List[str]) -> str:

        accumulator = []
        for text in strs:
            accumulator.append(str(len(text)))
            accumulator.append("#")
            accumulator.append(text)
        return "".join(accumulator)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
            
            word_size = int(s[i:j])
            word_start = j + 1
            word_end = word_start + word_size
            res.append(s[word_start:word_end])
            i = word_end
        
        return res