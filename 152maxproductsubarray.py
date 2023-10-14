class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        curmax,curmin = 1,1

        for i in nums:

            temp = curmax*i
            curmax = max(i*curmax,i*curmin,i)
            curmin = min(i*curmin,temp,i)
            res = max(curmax,res)

        return res
