#Find the position of first and last element in the sorted array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_index=self.findstartindex(nums, target)
        end_index=self.findendindex(nums, target)
        
        return [start_index, end_index]
    
    def findstartindex(self, nums: List[int], target: int) -> int:
        index=-1
        low=0
        high=len(nums)-1
        
        while low<=high:
            mid=low+(high-low)//2
            
            if nums[mid]==target:
                index=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
            
        return index
    
    def findendindex(self, nums:List[int], target: int) -> int:
        index=-1
        low=0
        high=len(nums)-1
        
        while(low<=high):
            mid=low+(high-low)//2
            
            if nums[mid]==target:
                index=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        
        return index