# Input from the user
text = input("Enter a string: ")

# Initialize an empty string
reversed_text = ""

# Loop through the original string from the end to the beginning
i = len(text) - 1
while i >= 0:
    reversed_text += text[i]
    i -= 1

# Print the reversed string
print("Reversed string:", reversed_text)
