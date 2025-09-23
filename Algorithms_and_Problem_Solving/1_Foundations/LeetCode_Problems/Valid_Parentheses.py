class Solution(object):
    def isValid(self, s):
        l=[]
        dic = {")":"(", "]":"[", "}":"{"}
        for ch in s:
            if ch in dic.values():
                l.append(ch)
            elif ch in dic.keys():
                if l==[] or l.pop() != dic[ch]:
                    return False
        
        return l==[]
        
        
       
