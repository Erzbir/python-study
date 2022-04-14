def get_sum(nums_n):
    nums_new = []
    b = 0
    num_sum = 0
    for a in nums_n:
        b += 1
        if a % 2 == 0:
            nums_new.append(b)
    for d in nums_new:
        num_sum += d
    return num_sum


nums = [1, 2, 3, 4, 5, 6]
print(get_sum(nums))
