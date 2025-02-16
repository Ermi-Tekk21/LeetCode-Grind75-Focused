class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna_seq = s
        dna_seq_size = len (dna_seq)
        tot_iteretion = dna_seq_size-9
        hash_map = {dna_seq[:10]: 1}

        for i in range (1, tot_iteretion):
            catch = dna_seq[i:10+i]
            if catch in hash_map.keys():
                hash_map[catch] += 1 
            else:
                hash_map[catch] = 1

        res=[]     
        for key, value in hash_map.items():
            if value > 1:
                res.extend([key])
                
        return (res)