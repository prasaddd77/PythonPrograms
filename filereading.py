# File IO Basics
"""
"r" - Open file for reading - default mode
"w" - Open file for writing
"x" - Creates file if not exists
"a" - Add more content to a file(Append)
"t" - Text mode
"b" - Binary mode
"+" - Read and write
"""

f = open("prasad.txt", "rt")
# print(f.readlines()) #To read the file as a list
# print(f.readline()) """To read the file one line at a time
# print(f.readline())    To read the file one line at a time
# print(f.readline())    To read the file one line at a time"""
# content = f.read()  # To read the entire file at once
# print(content)

for line in f:  # To read the file all at once using for loop
    print(line, end="")

# content = f.read(344455) #If you put a value inside the read function it will read that many contents of that file
# print("1", content)
#
# content = f.read(344455)
# print("2",content)


f.close()
