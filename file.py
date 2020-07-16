
#READ

# file = open('test.txt')

# Read all the contents of the file or n number of bytes
'''print(file.read(3))
print(file.readline())'''

# using readline print all line


'''line = file.readline()
while line != "":
    print(line)
    line = file.readline()'''

'''
lines = file.readlines()

for i in lines:
    print(i)
'''


#WRITE

with open('test.txt', 'r') as reader:
    lines = reader.readlines()
    reversedList = reversed(lines)
    with open('test.txt', 'w') as writer:
        for i in reversed(lines):
            writer.write(i)




# file.close()
