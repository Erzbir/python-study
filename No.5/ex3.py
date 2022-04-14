nums = [1,2,3,3,4,5]
def diff_nums(nums):
    b = 0
    for a in (1,len(nums)):
        b ^= a ^ nums[a]
        return b


b = diff_nums(nums)
print(b)