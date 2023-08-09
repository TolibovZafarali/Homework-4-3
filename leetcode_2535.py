class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        sum_elements = sum(nums)
        digits = []
        for i in range(len(nums)):
            if len(str(nums[i])) > 1:
                for m in str(nums[i]):
                    digits.append(int(m))
            else:
                digits.append(nums[i])
        
        return sum_elements - sum(digits)