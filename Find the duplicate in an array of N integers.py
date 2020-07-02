
Day1: (Arrays)

Find the duplicate in an array of N integers.(LEETCODE) 

#solution with time complexity o(nlogn) and space complexity o(n)
class Solution:
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

#solution with time complexity o(n) and space complexity o(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lst = set()
        for i in nums:
            if i in lst:
                return i
            lst.add(i)


#solution with time complexity o(n) and space complexity o(1)
#USING FLOYDS ALGORITHM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t = h = nums[0]
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if t == h :
                break
        t = nums[0]
        while t!= h:
            t = nums[t]
            h = nums[h]
        return t    
            
#solution with time complexity o(n) and space complexity o(1)
#USING HASHMAP #using XOR
