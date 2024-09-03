# in this tutorial, you will learn how to mainpulate directories in python using os module.

# get the current working directory
# the current working directory is the directory where the python script is running
# to get the current working directory, you use the os.getcwd() as follows:
import os

cwd = os.getcwd()
print(cwd)

# to change the current working directory, you use the function os.chdir():
    # os.chdir('/script')
    # print(f'{cwd}',cwd = os.getcwd())


