class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        while n!=0:
            count += n%2
            # n = n>>1#shifting towards right 1 bit 1011 -> 0101

        return count

        
