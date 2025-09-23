class Solution(object):
    def reverseString(self, s):
        j=1
        for i in range (len(s)/2):
            perm=s[i]
            s[i]=s[-j]
            s[-j]=perm
            j+=1
        return s


        
