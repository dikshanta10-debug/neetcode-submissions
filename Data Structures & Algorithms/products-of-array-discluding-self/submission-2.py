import math
from typing import List


class Solution:

  def productExceptSelf(self, nums: List[int]) -> List[int]:
    zero_count = nums.count(0)

    # Case 1: More than one zero -> all products will be 0
    if zero_count > 1:
      return [0] * len(nums)

    # Case 2: Exactly one zero -> only the index with 0 gets the product of other numbers
    if zero_count == 1:
      output = [0] * len(nums)
      prod = math.prod(num for num in nums if num != 0)
      output[nums.index(0)] = prod
      return output

    # Case 3: No zeros -> total product divided by each element
    total_prod = math.prod(nums)
    return [total_prod // num for num in nums]