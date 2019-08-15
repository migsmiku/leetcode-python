class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        x,y=0,0
        ans=''
        for s in target:
            m,n=divmod(ord(s)-ord('a'),5)
            while x<m:
                if x==4 and m==5:
                    while y>0:
                        ans+='L'
                        y-=1
                ans+='D'
                x+=1
            
            while x>m:
                ans+='U'
                x-=1
            while y<n:
                ans+='R'
                y+=1
            while y>n:
                ans+='L'
                y-=1
            
            ans+='!'
        return ans