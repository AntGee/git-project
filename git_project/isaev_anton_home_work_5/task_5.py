numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_num = set()
repeated_num = set()

for num in numbers:
    if num in repeated_num:
        continue
    if num in unique_num:
        repeated_num.add(num)
        unique_num.discard(num)
        continue
    unique_num.add(num)

print([num for num in numbers if num in unique_num])
