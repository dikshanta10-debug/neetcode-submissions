class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        encounter = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in encounter:
                return [encounter[complement],index]
            encounter[num] = index