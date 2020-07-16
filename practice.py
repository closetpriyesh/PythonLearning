courses = ['a', 'b', 'c', 'd', 'e']

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ', '.join(courses)

new_list = course_str.split(', ')

print(new_list)
print(courses)
print(course_str)

empty_list = list()

# Empty lists

empty_list = []
empty_list = list()

# Empty tuples

empty_tuple = ()
empty_tuple = tuple()

# Empty sets

empty_set = {}  # THIS ISN'T RIGHT. It's a dict
empty_set = set()

# dictionaries key can be any immutable data type like strings, int


dict = {'name': 'priyesh', 'age': 23}

print(dict.get('nae', 'Not found'))

print(dict.keys())
print(dict.values())
print(dict.items())

for key, value in dict.items():
    print(key, value)


# False values : False, None, Zero of any numeric type, any empty sequence(ex - '', [], ()), any empty mapping({})


def func(greeting):
    return f'{greeting} function'


print(func('Hi'))
