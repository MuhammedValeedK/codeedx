# Armstrong Number Checker

num = int(input("Enter a number: "))
num_str = str(num)
num_length = len(num_str)
sum = 0

for digit in num_str:
    sum += int(digit) ** num_length

if sum == num:  
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

