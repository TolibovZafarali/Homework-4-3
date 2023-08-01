class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            ans.append(nums[i])
        return ans
result = Solution()
print(result.buildArray([0,2,1,5,3,4]))
print(result.buildArray([5,0,1,2,3,4]))