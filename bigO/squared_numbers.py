def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    print(squared_numbers)
    return squared_numbers

numbers = [2,5,8,9]
get_squared_numbers(numbers)