str = 'Good Morning'
str1 = 'Good'
str2 = 'Bad'

if str == 'Good Morning':
    print(str)
elif str1 == 'Good':
    print(str1)
else:
    print(str2)

# for loop

obj = [2, 3, 5, 7, 8]

for i in obj:
    print(i)

for i in range(6):
    print(i)

# while

i = 10

while i > 1:
    print(i)
    if i == 3:
        break
    i -= 1
