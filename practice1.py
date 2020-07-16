import calendar
import datetime
import random

courses = ['History', 'Math', 'Science']

print(random.choice(courses))

print(datetime.date.today())
print(calendar.isleap(2020))


def func(name, age=23):
    print(f'My name is {name} and age is {age}')


def func(*args, **kwargs):
    print(args)
    print(kwargs)


names = ('a', 'b', 'c')

dict = {'a': 'b', 'b': 'c', 'c': 'd'}

func('Priyesh', **dict)

list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(list[::-1])

sample_url = 'http://coreyms.com'

print(sample_url[::-1])

print(sample_url[7:])

print(sample_url[:-4])





