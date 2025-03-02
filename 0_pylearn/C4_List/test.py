def find_elements(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    unique_elements = [num for num in frequency if frequency[num] == 1]
    unique_elements.sort()
    
    if unique_elements:
        return unique_elements
    else:
        return False

input_1 = input().strip('[]')
input_list = [int(x) for x in input_1.split(',')]

result = find_elements(input_1)
if result:
    print(', '.join(map(str, result))) 
else:
    print(result)