numbers = 15


def nums_gen():
    for num in range(1, numbers + 1, 2):
        yield num


nums = nums_gen()
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
