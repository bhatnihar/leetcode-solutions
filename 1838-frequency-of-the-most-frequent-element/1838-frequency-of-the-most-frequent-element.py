from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)
        left = 0
        total = 0
        maxFreq = 1

        for right in range(n):
            total += nums[right]

            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1

            maxFreq = max(maxFreq, right - left + 1)

        return maxFreq