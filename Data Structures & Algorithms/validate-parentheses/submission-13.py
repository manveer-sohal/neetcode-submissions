class Solution:
    def isValid(self, s: str) -> bool:
  
        PARENTHESES = {'(':')', '{':'}', '[':']'}
        stack = []


        for char in s:
            if char in PARENTHESES:
                stack.append(char)
            else:
                if stack:
                    if PARENTHESES[stack.pop()] != char:
                        return False
                else:
                    return False
        
        return False if len(stack) > 0 else True




        