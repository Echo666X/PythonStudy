s = input()

num_count = 0
lower_case_letters = ''

for char in s:
    if char == '#':
        break
    elif char.isdigit():
        num_count += 1
    elif char.islower():
        lower_case_letters += char

print("{},{}".format(num_count, len(lower_case_letters)))
print(lower_case_letters)
