class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        

        ret = [0 for _  in range(len(temperatures))]

        stack = []

        for r in range(len(temperatures)):
            curr = temperatures[r]
            while stack and curr > temperatures[stack[-1]]:

                index = stack.pop()
                days = r - index
                ret[index] = days
        
            stack.append(r)
        

        return ret



            


