def clean(s: str) -> str:
    new_s = [c.lower() for c in s if c.isalnum()]
    return ''.join(new_s)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = clean(s)
        n = len(s)
        if n>0:
            l, r = 0, n-1
            while (l<r):
                if (s[l]==s[r]):
                    l+=1
                    r-=1
                else: 
                    return False
        return True
            


    

