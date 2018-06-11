def subarray_sum(nums, k):
    solution = 0
    nums_len = len(nums)
    print nums_len
    for start_index in xrange(nums_len):
        print 'Iteration: ', start_index
        for index in xrange(start_index, nums_len):
            if start_index == 0:
                if index > 0:
                    nums[index] = nums[index] + nums[index-1]
            else:
                nums[index] = nums[index] - nums[start_index-1]
               
            if nums[index] == k:
                solution += 1
        print nums
         
    return solution
