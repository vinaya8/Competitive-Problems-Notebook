#Find longest substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_position={}
        start=0
        max_length=0
        for end in range(len(s)):
            
            if s[end] in last_position:
                start=max(start, last_position[s[end]]+1)
            
            last_position[s[end]]=end
                
            
            max_length=max(max_length, end-start+1)
        
        return max_length