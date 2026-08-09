class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        ans = 0
        count = 0

        for i in range(len(nums)):
            if(nums[i] == 0):
                count = 0

            else:
                count += 1

            if(count > ans):
                ans = count

        return ans



         