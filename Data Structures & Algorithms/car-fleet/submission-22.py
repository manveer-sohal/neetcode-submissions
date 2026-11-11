class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        
        #Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]




    #     55--5--5----
    #    115  2  10


        time_till_end = []

        for pos,v in sorted(zip(position,speed), key =lambda x: x[0]):
          

            temp = (target - pos) / v
           

            
            while time_till_end and temp >= time_till_end[-1]:
                time_till_end.pop()
            time_till_end.append(temp)
          
        
        return len(time_till_end)





       


        # car can only catch up if it is faster or as fast & part of same fleet as car ahead of it.


