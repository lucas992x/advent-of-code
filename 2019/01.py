nums = []
with open('01.txt', 'r') as file:
    for line in file:
        nums.append(int(line))
n = len(nums)
# Part 1
for i in range(n - 1):
    for j in range(i + 1, n):
        a = nums[i]
        b = nums[j]
        if a + b == 2020:
            print('{} + {} = 2020\n{} * {} = {}'.format(a, b, a, b, a * b))
# Part 2
for i in range(n - 1):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a = nums[i]
            b = nums[j]
            c = nums[k]
            if a + b + c == 2020:
                print('{} + {} + {} = 2020\n{} * {} * {} = {}'.format(a, b, c, a, b, c, a * b * c))
