numbers = [1, 2, 3, 4, 122]
n = 3

power = lambda numbers, n: [num**n for num in numbers]
print(power(numbers, n))