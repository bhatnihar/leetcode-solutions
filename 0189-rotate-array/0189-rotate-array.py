class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        temp = []

        # Store last k elements
        for i in range(n - k, n):
            temp.append(nums[i])

        # Shift remaining elements to the right
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]

        # Put temp elements at the beginning
        for i in range(k):
            nums[i] = temp[i]
        

        