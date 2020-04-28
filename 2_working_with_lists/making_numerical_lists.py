# 4.3 - Counting to Twenty
for num in range(1, 21):
    print(num)

# 4.4 - One Million
nums = list(range(1, 1000001))
# for num in nums:
#     print(num)

# 4.5 - Summing a Million
print('Min:', min(nums))
print('Max:', max(nums))
print('Sum:', sum(nums))

# 4.6 - Odd Numbers
odd_numbers = list(range(1, 20, 2))
for odd in odd_numbers:
    print(odd)

# 4.7 - Threes
mult_list = list(range(3, 31, 3))
for num in mult_list:
    print(num)

# 4.8 - Cubes
cubes = []
for num in range(1, 11):
    cube = num ** 3
    cubes.append(cube)
    print(cube)

# 4.9 - list comprehension
cubes_list = [value**3 for value in range(1, 11)]
print(cubes_list)
