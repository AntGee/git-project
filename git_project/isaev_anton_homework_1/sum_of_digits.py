numbers = []
sum_numbers = []

for num in range(1, 1001, 2):
    numbers.append(num ** 3)

print(numbers)

for number in numbers:
    sum_number = 0
    while number:
        sum_number += number % 10
        number = number // 10
        if sum_number % 7 == 0:
            sum_numbers.append(number)

print(sum(sum_numbers))

sum = 0

for number in numbers:
    sum_number = 0
    number += 17
    while number:
        sum_number += number % 10
        number = number // 10
        if sum_number % 7 == 0:
            sum += number

print(sum)
