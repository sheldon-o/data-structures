'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]'''
nums=[0,1,0,3,12]

    def moveZeroes(nums):
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
        """
        Do not return anything, modify nums in-place instead.
        """
    moveZeros(nums)



#second method faster
def moveZero(nums):
  index = 0
        
        for n in nums: 
            if(n != 0): 
                nums[index] = n
                index += 1
        
        for i in range(index, len(nums)): 
            nums[i] = 0


