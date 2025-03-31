class Solution:
    def search(self, a: List[int], target: int) -> bool:
        low,high = 0,len(a)-1
        while low<=high:
            mid = (low+high)//2
            if a[mid]==target:
                return True
            # Additional check for duplicates
            while mid<high and a[mid]==a[high]:
                high-=1
            if a[mid]<=a[high]:
                if a[high]<target or target<a[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if a[mid]<target or target<=a[high]:
                    low = mid+1
                else:
                    high = mid-1
        return False