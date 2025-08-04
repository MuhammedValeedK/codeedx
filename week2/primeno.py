# Check if prime number


num = int(input("Enter a number to check prime: "))

is_prime = True

if num <=1:
    is_prime = False
else:
    i = 2
    while num > i:
        if  num % i == 0:
         is_prime = False
        break
    i+1



if is_prime == False:
    print(f"{num} is not prime number")

else:
   print(f"{num} is prime number")
    

