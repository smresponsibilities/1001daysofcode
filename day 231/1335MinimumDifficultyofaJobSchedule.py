class Solution:
    def minDifficulty(self, j: List[int], d: int) -> int:
        n=len(j)
        if d>n:  
            return -1
        if d==n: 
            return sum(j)
        @lru_cache(maxsize=231)
        def F(i,a,b) :
            if i==n and a==0: 
                return 0
            if i==n or a==0: 
                return 9000000000
            b=max(b,j[i]) 
            return min(b+F(i+1,a-1,0),F(i+1,a,b))    
        return F(0,d,0)