# Fibonacci series up to N terms

n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0

print("Fibonacci Series:")
while count < n:
    print(a)
    a, b = b, a + b
    count += 1

# Print a triangle pattern of stars

row = 10

for i in range(1, row + 1):
    for j in range(1, i+1):
        print("*", end=" ") 
    print()

# Find the sum of digits of a number

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num //= 10

print("Sum of digits:", sum)

# Check if a string is a palindrome

text = input("Enter a string: ")

reversed_text = text[::-1]  

if text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Count the number of words in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
count = len(words)
print("Number of words:", count)

# Generate a multiplication table from 1 to 10

num = int(input("Enter a number to get it's multiplication table: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

# Print only unique characters from a string

s = "programming"
for char in s:
    if s.count(char) == 1:
        print(char, end=" ")

