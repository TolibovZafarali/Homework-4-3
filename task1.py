class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        concatenation = []
        for n in nums:
            concatenation.append(n)
        nums.extend(concatenation)
        return nums
result = Solution()

print(result.getConcatenation([1 ,2, 1]))
print(result.getConcatenation([1, 3, 2, 1]))