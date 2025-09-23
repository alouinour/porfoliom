class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        string=""
        for i in range(len(s)):
            if s[i].isalnum():
                string += s[i]
        n=len(string)
        left=0
        right=n-1
        while left<right:
            if string[left] != string[right]: 
                return False
            left+=1
            right-=1
        return True

        
