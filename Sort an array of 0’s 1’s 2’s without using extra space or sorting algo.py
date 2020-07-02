Day1: (Arrays)

Sort an array of 0’s 1’s 2’s without using extra space or sorting algo (LEETCODE = colorSort)

#Using counting sort time complexity o(n) and space complexity o(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r,w,b = 0,0,0
        for i in nums:
            if i == 0:
                r+=1
            elif i == 1:
                w+=1
            elif i ==2:
                b+=1
        for i in range(len(nums)):
            if r>0:
                nums[i] = 0
                r-=1
            elif w>0:
                nums[i] = 1
                w-=1
            elif b>0:
                nums[i] = 2
                b-=1

# Using 3 pointers having space complexity o(1) and time complexity o(n)       
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums)-1
        while mid<=high:
            if  nums[mid] == 0:
                nums[mid],nums[low] = nums[low],nums[mid]
                mid+=1
                low+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1
