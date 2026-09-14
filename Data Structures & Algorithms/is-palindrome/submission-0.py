import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag = True
        s = s.lower()
        s = s.replace(" ", "")
        s = s.translate(str.maketrans('', '', string.punctuation))

        if s == s[::-1]:
            flag = True
        else:
            flag = False

        return flag