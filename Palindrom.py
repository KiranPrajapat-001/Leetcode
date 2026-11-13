
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        return x == int(str(x)[::-1])


x = int(input("Enter a number: "))

obj = Solution()
print(obj.isPalindrome(x))
