class Solution:

  def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
      return 0

    ordered = sorted(set(nums))
    longest = 1
    current_streak = 1

    for i in range(len(ordered) - 1):
      if ordered[i] + 1 == ordered[i + 1]:
        current_streak += 1
      else:
        current_streak = 1  # Reset streak if there's a gap

      longest = max(longest, current_streak)

    return longest