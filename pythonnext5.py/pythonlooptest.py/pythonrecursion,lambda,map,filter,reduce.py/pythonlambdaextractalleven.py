numbers = [10, 15, 20, 25, 30]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original list:", numbers)
print("Even numbers:", even_numbers)