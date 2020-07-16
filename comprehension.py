
nums = [1, 2, 3, 4, 5]

list = [n for n in nums if n%2 == 0]

print(list)


my_list = [(letter, num) for letter in 'abcd' for num in range(4)]

print(my_list)

'''
map_list = map(lambda n: n*n, nums)

for key in map_list:
    print(key)
'''

# filter_list = filter(lambda n: n%2 ==0, nums)

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

print(zip(letters, numbers))

for y, z in zip(letters, numbers):
    print(y, z)


my_dict = { letter: number for (letter, number) in zip(letters, numbers)}

print(my_dict)

dnums = [1,1,1,2,2,3,3,3]

my_set = {n for n in dnums}
print(my_set)

'''
def gen_func(nums):
    for n in nums:
        yield n*n
'''

# my_gen = gen_func(nums)

my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)


