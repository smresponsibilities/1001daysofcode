class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(maxsize=230)
        def F(a,b,c,d):
            if a==len(s):
                return 0
            if s[a]==b:
                e=F(a+1,b,c+1,d)+(c in [1,9,99])
            else:
                e=1+F(a+1,s[a],1,d)
            if not d:
                return e
            else:
                return min(e,F(a+1,b,c,d-1))

        return F(0,"sm",0,k)