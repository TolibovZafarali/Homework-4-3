class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        myList = []
        
        for i in range(len(s)):
            myList.append(s[i])
        
        myDict = dict(zip(indices, myList))

        sorted_dict = dict(sorted(myDict.items()))

        return ''.join(list(sorted_dict.values()))

result = Solution()
print(result.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))