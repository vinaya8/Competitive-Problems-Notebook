#Find how many Stones in S are Jewels J

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        hash_table={}
        for i in J:
            hash_table[ord(i)]=1
        c=0
        for i in S:
            if ord(i) in hash_table:
                c=c+1
        
        return c