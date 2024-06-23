# in this tutorial, you learn various ways to read text files in Python.

# the following shows how to read all texts from the readme.txt file into a string:
# with open('readme.txt') as f:
#     lines = f.readlines()

# to read a text file in python, you follow thes e steps:
    # open a text file for reading by using the open() function
    # second, read text from the text file usng the file  read(), readline() or readlines() method of the fil object
    # third  , close the file using the file close() method


# 1)open() function
    # the open() function has many parameters but you will be focusing on the first two:
    # open(path_to_file, mode)
    
    # if the program and file are in the same folder, you need to specify only the filename of the file
    # otherwise, you need to include the path to the file as well as the filename.
    # to specify the path to the file, you use the /
    
    # the mode is an optional parameter, it is a string that specifies the mode in which you want to open the file
    # 'r' means open for text file for reading text
    # 'w' means open a text file for writing text
    # 'a' means open a text file for appending text
    
    # the open() function returns a file object which you will use to read text from a text file
    
# 2) reading text methods 
    # read(size) – read some contents of a file based on the optional size and return the contents as a string. If you omit the size, the read() method reads from where it left off till the end of the file. If the end of a file has been reached, the read() method returns an empty string.
    # readline() – read a single line from a text file and return the line as a string. If the end of a file has been reached, the readline() returns an empty string.
    # readlines() – read all the lines of the text file into a list of strings. This method is useful if you have a small file and you want to manipulate the whole text of that file.

# 3) close() methods
     # the file that you open will remain open until you close it using the close() method
     # it is important to close the file that is no longer in use
     # it should be noted that, python provides the with statement to automatically manage the file context
     # when the with statement block ends, the file is automatically closed
     
     

# reading a text file examples
# we will use the-zen-of-python.text file for the demonstration

with open('D:/Code/Python/PythonStudy/1_PythonTutorial/PythonBasic/Section_12_Working with Files/the-zen-of-python.txt') as f:
    contents = f.read()
    print(contents)
    
with open('D:/Code/Python/PythonStudy/1_PythonTutorial/PythonBasic/Section_12_Working with Files/the-zen-of-python.txt') as f:
    [print(line) for line in f.readlines()]
# in the second example, you can see a blank line after each line from a file is that each line in the text file has a newline character(\n)


# a more concise way to read a text file line by line
# you can use a for loop to iterate over the lines of a text file:
with open('D:/Code/Python/PythonStudy/1_PythonTutorial/PythonBasic/Section_12_Working with Files/the-zen-of-python.txt') as f:
    for line in f:
        print(line.strip())
        

# the code in the previous examples works fine with ASCII text files, however, if you are dealing with other languages such as japanese, chinese ad korean. the text file is not a simple ascii text file
# And it’s likely a UTF-8 file that uses more than just the standard ASCII text characters.
# to open it, you need to pass the encoding= 'utf-8' to the open() function to instruct it to expect UTF-8 characters