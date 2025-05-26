# Label the program written in problem 4 with comments.

import os

# select the directory whose content you want to list
path = '/C Coding'

# use the os module to list the diectory content
contents = os.listdir(path)

# print the contants  of the directory
for item in contents:
    print(item)
