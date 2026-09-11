class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        sett = set(nums) 
        return(sorted(list(sett)) != sorted(nums))
            
