class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_sort = ''.join(sorted(s)) 
        t_sort = ''.join(sorted(t)) 
        
        if s_sort == t_sort : 
            flag = True 
        else: 
            flag = False
        
        return flag
        
