class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        sum=0
        oneFeq = []
        for i in bank:
            devNo =  i.count('1')
            if devNo != 0:
                oneFeq.append(devNo)
        for i in range(len(oneFeq)-1):
            sum += oneFeq[i]*oneFeq[i+1]
        return sum