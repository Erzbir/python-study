def diff_nums(nums_x):
    c = 0
    for a in (1, len(nums_x)):
        c ^= a ^ [a]
        return c


nums = [1, 2, 3, 3, 4, 5]
b = diff_nums(nums)
print(b)
