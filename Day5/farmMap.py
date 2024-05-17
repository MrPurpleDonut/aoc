class farmMap:

    def __init__(self, rangeMap: list ):
        self.rangeMap = rangeMap

    def transform(self, location: int)->int:
        for map in self.rangeMap:
            if(location >= map[1] and location < map[1]+map[2]):
                return map[0]-map[1]+location
            
        return location
    
    def processRanges(self, rangeToCheck: list)->list:
        slicedRanges =[]
        notCarved = True
       
        for map in self.rangeMap:
            if(rangeToCheck[0] >= map[1] and rangeToCheck[0] < map[1]+map[2]):
                #Bottom of range is in middle of map range
                if(rangeToCheck[0] + rangeToCheck[1] <= map[1]+map[2]):
                    #We are contained
                    slicedRanges.append([map[0]-map[1]+rangeToCheck[0], 
                                         rangeToCheck[1]])
                else:

                    #Our top is above
                    slicedRanges.append([map[0]-map[1]+rangeToCheck[0], 
                                         map[2]+map[1]-rangeToCheck[0]])
                    slicedRanges.extend(self.processRanges([map[1]+map[2], 
                                                            rangeToCheck[0]+rangeToCheck[1]-map[1]-map[2]]))
                    
                notCarved = False
                break

            elif(rangeToCheck[0] + rangeToCheck[1] > map[1] and rangeToCheck[0] + rangeToCheck[1] <= map[1]+map[2]):
                #Bottom of range below bottom and upper is in middle of range
                slicedRanges.append([map[0],rangeToCheck[0]+rangeToCheck[1]-map[1]])
                slicedRanges.extend(self.processRanges([rangeToCheck[0],rangeToCheck[1]-(rangeToCheck[0]+rangeToCheck[1]-map[1])]))
                notCarved = False
                break

            elif(rangeToCheck[0]< map[1] and rangeToCheck[0] +rangeToCheck[1] >= map[1]+map[2]):
                slicedRanges.append([map[0],map[2]])
                slicedRanges.extend(self.processRanges([rangeToCheck[0],rangeToCheck[1]-(rangeToCheck[0]+rangeToCheck[1]-map[1])]))
                slicedRanges.extend(self.processRanges([map[1]+map[2], 
                                                            rangeToCheck[0]+rangeToCheck[1]-map[1]-map[2]]))
                notCarved = False
                break


        if notCarved:
            slicedRanges.append(rangeToCheck)
        return slicedRanges
    
