def twoSum(nums, target):

    for i in nums:
        j = target - i
        start_index = nums.index(i)
        next_index = start_index + 1
        temp_nums = nums[next_index: ]
        if j in temp_nums:
            return(nums.index(i),next_index + temp_nums.index(j))

nums=[2,7,11,15]
target=9
twoSum(nums, target)