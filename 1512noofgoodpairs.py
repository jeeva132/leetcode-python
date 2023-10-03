class Solution:
    
    def numIdenticalPairs(self, nums: List[int]) -> int:

        def fact(n):
            fact = 1
            while n>0:
                fact = fact*n
                n = n-1
            return fact
        count = 0
        dict1 ={}
        for i in nums:
            if i not in dict1:
                dict1[i] =1
            else:
                dict1[i] +=1

        arr = []
        for i in dict1.values():
            arr.append(i)
        for i in arr:
            num = fact(i)
            den = fact(i-2)*2
            count +=int(num/den)

        if sum(arr) == len(arr):
            return 0
        return int(count)
