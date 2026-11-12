class TimeMap:

    def __init__(self):
        self.value = {}
        #name: [ ]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value.setdefault(key,[]).append((value,timestamp))
    

    def get(self, key: str, timestamp: int) -> str:


      
        array = self.value.get(key,[])
        ret = ""
        

      
     
    
        l = 0 #start time
        r = len(array) - 1 #end time
       

        m = 0
        while l <= r:
            m = (l + r + 1)//2

            if array[m][1] > timestamp:
                r = m -1

            elif array[m][1] <= timestamp:
                ret = array[m][0]
                l = m + 1
            else:
                return array[m][0]
       
       
        # print(l,array)
        return ret
    
            
        


# name: [1:emotion, 2:emotion]