import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            tar = target - numbers[i]

      # Search only in the remaining portion of the array to the right of i
            idx = bisect.bisect_left(numbers, tar, i + 1)

      # Check if tar was actually found in the remaining portion
            if idx < len(numbers) and numbers[idx] == tar:
                return [i + 1, idx + 1]
            