class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []

        binary = bin(n)[2:] 
        for i in range(n + 1): # fix1
            binary = bin(i)[2:] #fix2

            cnt = 0
            for one in binary:
                if one == '1':
                    cnt += 1 
            
            lst.append(cnt)

        return lst