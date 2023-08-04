class Solution:
    def isHappy(self, n: int) -> bool:
        used = []

        while n > 0:
            tmp = 0
            while n > 0:
                i = n % 10
                tmp = tmp + i ** 2
                n = n // 10
            if tmp in used:
                return False
            else:
                used.append(tmp)
            
            if tmp == 1:
                return True
            
            n = tmp

        return False

        
result = Solution()
print(result.isHappy(19))
print(result.isHappy(2))