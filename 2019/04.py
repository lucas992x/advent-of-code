import re

input = '152085-670283'  # my puzzle input
counter1 = 0
counter2 = 0
for password in range(int(input[:6]), int(input[7:]) + 1):
    nums = [int(d) for d in [c for c in str(password)]]
    if nums[1] >= nums[0] and nums[2] >= nums[1] and nums[3] >= nums[2] and nums[4] >= nums[3] and nums[5] >= nums[4]:
        # Part 1
        if re.search(r'(\d)\1', str(password)):
            counter1 += 1
        # Part 2
        for num in set(nums):
            if nums.count(num) == 2:
                counter2 += 1
                break

print(counter1)
print(counter2)
