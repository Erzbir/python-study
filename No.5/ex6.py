def get_sum(nums):
    c = []
    b = 0
    sum = 0
    for a in nums:
        b += 1
        if a%2 == 0:
            c.append(b)
    for d in c:
        sum += d    
    return sum

nums = [1,2,3,4,5,6]
print(get_sum(nums))