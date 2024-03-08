class Solution:
    def removeConsecutiveCharacter(self, S):
        
        ans=[]
        prev=''
        for i in S:
            if i!=prev:
                ans.append(i)
                prev=i
        return ''.join(ans)

  # Question link: https://www.geeksforgeeks.org/problems/consecutive-elements2306/1
