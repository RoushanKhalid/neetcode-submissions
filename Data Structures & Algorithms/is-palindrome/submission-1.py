import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag = True
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)

        if s == s[::-1]:
            flag = True
        else:
            flag = False

        return flag