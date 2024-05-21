num = int(input())

divisible_by_5 = num % 5 == 0
divisible_by_7 = num % 7 == 0
divisible_by_11 = num % 11 == 0

if divisible_by_5 and divisible_by_7 and divisible_by_11:
    print(f"{num} can divided by 5,7 and 11.")
elif divisible_by_5 and divisible_by_7:
    print(f"{num} can divided by 5,7.")
elif divisible_by_5 and divisible_by_11:
    print(f"{num} can divided by 5.")
    print(f"{num} can divided by 11.")
elif divisible_by_7 and divisible_by_11:
    print(f"{num} can divided by 7,11.")
elif divisible_by_5:
    print(f"{num} can divided by 5.")
elif divisible_by_7:
    print(f"{num} can divided by 7.")
elif divisible_by_11:
    print(f"{num} can divided by 11.")
else:
    print(f"{num} can not divided by 5,7 or 11.")
