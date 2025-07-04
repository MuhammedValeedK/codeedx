# Input: list of numbers from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Assume first number is both largest and smallest
largest = numbers[0]
smallest = numbers[0]

# Loop through the list
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Output the results
print("Largest number is:", largest)
print("Smallest number is:", smallest)

