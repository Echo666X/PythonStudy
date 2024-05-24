string_input = input()
str_dict = {}

for char in string_input:
    str_dict[char] = str_dict.get(char,0) + 1
    
for key,value in str_dict.items():
    if value == 1:
        print(key)
        break
    
else:
    print('no')