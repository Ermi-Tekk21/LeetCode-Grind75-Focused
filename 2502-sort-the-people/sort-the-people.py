class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        namedHeights = list((key, value) for key, value in zip(names, heights))
        size = len(heights)
        for i in range (size-1):
            for j in range (0, size-i-1):
                if (heights[j] > heights [j+1]):
                    heights [j], heights [j+1] = heights[j+1], heights[j]
        listedName=[]
        for i in heights:
            print (i)
            for j in range (len(namedHeights)): 
                    if namedHeights[j][1] == i:
                        listedName.append(namedHeights[j][0])
        size = len(listedName)
        res = []
        for i in range (size):
            res.append(listedName[-i-1])
                        
        return (res)