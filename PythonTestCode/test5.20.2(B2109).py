input_string = input()
num_digit = 0
for str in input_string:
    if str.isdigit():
        num_digit += 1
        
print(f"{num_digit}")