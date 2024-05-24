#Summary: in this tutorial, you’ll learn about Python string and its basic operations.

#anything inside quotes is a string
#you can use either single or double quotes

message = 'This is a string in Python'
print(message)
message = "This is also a string"
print(message)
message = "It's a string"
print(message)
message = '"Beautiful is better than ugly.". Said Tim Peters'
print(message)
message = 'It\'s also a valid string'
print(message)

# when building a program, you always need to check the type of a string, you can use is__() method like this:
# isalpha(): 检查字符串是否只包含字母。
# isdigit(): 检查字符串是否只包含数字。
# isalnum(): 检查字符串是否只包含字母和数字，不包含空格或其他特殊字符。
# isspace(): 检查字符串是否只包含空格、制表符、换行符等空白字符。
# islower(): 检查字符串是否全部由小写字母组成。
# isupper(): 检查字符串是否全部由大写字母组成。
# istitle(): 检查字符串中的每个单词是否首字母大写，其余字母小写（标题格式）。
# startswith(prefix): 检查字符串是否以指定的前缀开头。
# endswith(suffix): 检查字符串是否以指定的后缀结尾。