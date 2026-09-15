class Solution:
    def hammingWeight(self, n: int) -> int:
        
        binary = bin(n)[2:]
        lst = []

        for i in binary:
            lst.append(i)

        cnt = 0

        for i in lst:
            if i == '1':
                cnt += 1

        return cnt