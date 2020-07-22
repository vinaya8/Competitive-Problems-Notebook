#Search in a sorted arary of unknown size

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0)==target:
            return 0
        
        left,right=0,1
        while target>reader.get(right):
            left=right
            right<<=1
        
        while left<=right:
            mid=left+(right-left)//2
            #mid=left+((right-left)>>1)
            num=reader.get(mid)
            
            if num == target:
                return mid
            elif num>target:
                right=mid-1
            else:
                left=mid+1
        
        return -1