class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def freq_sliding_win(cont_array_size):
            k=3
            sum = 0
            for i in range (1,cont_array_size-k+2):
                sum += i
            return (sum)
        tot_freq = 0
        len_cont_array = 2
        
        for i in range (1, len(nums)-1):
            ub = nums[i+1] - nums[i]
            lb = nums[i] - nums[i-1]
            
            
            if ub == lb:
                len_cont_array +=1
                
            else:
                tot_freq += freq_sliding_win(len_cont_array)
                len_cont_array = 2
                
        tot_freq += freq_sliding_win(len_cont_array)
        return (tot_freq)