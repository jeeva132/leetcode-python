class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dict1 = {'(':')','[':']','{':'}'}

        for i in s:
            if i in dict1:
                stack.append(i)
            elif len(stack)==0 or dict1[stack.pop()]!= i:
                return False

        if len(stack) == 0:
            return True
