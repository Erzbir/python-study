#冒泡
def bubble_sort(nums):
    for index_i in range(len(nums)):
        for index_n in range(len(nums)-1):
            if nums[index_i] > nums[index_n]:
               nums[index_i] = nums[index_i] ^ nums[index_n]
               nums[index_n] = nums[index_i] ^ nums[index_n]
               nums[index_i] = nums[index_i] ^ nums[index_n]
    return nums


#选择
def select_sort(nums):
    for index_i in range(0,len(nums)-1):
        max = index_i
        for index_n in range(index_i+1,len(nums)):
            if nums[index_n] > nums[max]:
                max = index_n
        if max !=index_i:
            nums[index_i] = nums[index_i] ^ nums[max]
            nums[max] = nums[index_i] ^ nums[max]
            nums[index_i] = nums[index_i] ^ nums[max]
    return nums


#插入
def insert_sort(nums):
    for index_i in range(len(nums)-1):
        for index_n in range(index_i+1,len(nums)):
            if nums[index_i] < nums[index_n]:
                nums.insert(index_i,nums[index_n])
    return nums




nums=[1,2,3,4,5,6,7]
print(f"排序前:{nums}")
print(f"冒泡排序后:{bubble_sort(nums)}")
print(f"选择排序后:{select_sort(nums)}")
print(f"插入排序后:{insert_sort(nums)}")