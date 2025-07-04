# Input: original list
original_list = []
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
original_list.extend(numbers)

# Empty list to store unique values
unique_list = []

# Loop through the original list
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

# Print the result
print("List after removing duplicates:", unique_list)
