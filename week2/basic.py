## Print all characters in a string

# s = "Hello"
# for char in s:
#     print(char)

# # Sum of numbers from 1 to 100
# total = 0
# for i in range(1, 101):
#     total += i
# print("Sum:", total)

# #Count the number of vowels in a string
# s = "Muhammed Valeed"
# vowels = "aeiouAEIOU"
# count = 0
# for char in s:
#     if char in vowels:
#         count += 1
# print("Vowel count:", count)


# # Find the factorial of a number
# num = 5
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial:", factorial)

# # Print all elements of a list using a loop

lst = [1, 2, 3, 4]
for item in lst:
    print(item)

## Reverse a string
# s = "Kozhikode"
# reversed_s = ""
# for char in s:
#     reversed_s = char + reversed_s
# print(reversed_s)


## Check if a number is prime
num = 11
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    
