# Find the Largest and Smallest Number in a List 

numbers = list(map(int, input("Enter numbers seperated by spaces: ").split()))
print (numbers)

largest = max(numbers)
smallest = min(numbers)

print("Largest number is:", largest)
print("Smallest number is:", smallest)