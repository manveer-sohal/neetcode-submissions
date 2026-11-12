class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:



        stack = []
        #idx,height
        
        # heights = [7,1,7,2,2,4]
        ret = 0

        for idx, height in enumerate(heights):

            temp_idx = idx
            while stack and height <= stack[-1][1]:
                temp_idx , _ = stack.pop()

            stack.append((temp_idx,height))

            for cidx, xh in stack:

                ret = max(ret, (idx-cidx + 1) * xh)

            # print(stack,ret)

        return ret





        # [0,0,2,2,2,]
        #  7 7 7 7 7
        #  7 7 7 7 7



