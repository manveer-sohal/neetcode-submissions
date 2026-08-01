class Solution:

    def encode(self, strs: List[str]) -> str:


        encoded = []
        for words in strs:
            encoded.append(str(len(words)))
            encoded.append("#")
            encoded.append(words)

        
        
        return "".join(encoded)





# 5#5abcd
    def decode(self, s: str) -> List[str]:
        ret = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])
            
            i=j+1

            ret.append(s[i:i+length])
            i = i + length
        return ret



            




















#         encoded =[]
#         for word in strs:
#             encoded.append(str(len(word)))
#             encoded.append("#")
#             encoded.append(word)
#         return "".join(encoded)

# #5#Hello5#World

#     def decode(self, s: str) -> List[str]:
#         decoded = []
#         i = 0
#         while i < len(s):
#             j = i
#             while s[j]!='#' :
#                 j+=1
#             length  = int(s[i:j])
#             i = j +1
#             decoded.append(s[i:length + i])
#             i +=length
            
#         return decoded




