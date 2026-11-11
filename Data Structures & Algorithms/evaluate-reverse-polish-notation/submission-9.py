class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        
        stack = []

        OPERATORS = {'+', '-', '*', '/'}

        ret = 0


        for char in tokens:
            if char in OPERATORS:
                b = stack.pop()
                a = stack.pop()

                if char == "+":
                    ret = a + b
                
                elif char == "-":

                    ret = a - b

                elif char == "*":

                    ret = a * b

                elif char == "/":
                    ret = int(a / b)
                
                
                stack.append(ret)
            
            else:
                stack.append(int(char))
               
            
          

        
        return stack[-1]