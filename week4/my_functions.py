#Simple function without parameters
def welcome():
 print("Welcome")
welcome()

#Function with parameters (eg: mathematical operations)
def addition(a,b):
 return a+b 
print ("sum:", addition(5,3))
 
# Function with default parameters
def power(num,exp=2):
 return num ** exp

print("Square:",power(6))
print("qube:",power(6,3)) 

# Function returning multiple values

def calculations (a,b):
 return a+b, a-b, a*b, a/b

add,sub, mul, div = calculations(15,5)
print(add,sub,mul,div)

# Function with variable number of argument

def total_sum(*numbers):
 return sum(numbers)
print("sum:",total_sum(12,14,16,18,1,5))

# Recursive function (Factorial)    resursive-swyam vilikkunnu

    #The factorial of a number (denoted as n!) is a mathematical operation that represents the product of all positive integers from 1 to that number.
    #Similarly, 5! = 5 × 4 × 3 × 2 × 1 = 120  (facto(5) = 5 * facto(4)
    #(facto(4) = 4 * facto(3), facto(3) = 3 * facto(2),facto(1) = 1 * facto(0), facto(0) = 1 (base case reached!)))
    #facto(0) returns 1, facto(1) returns 1 * 1 = 1, facto(2) returns 2 * 1 = 2, facto(3) returns 3 * 2 = 6, facto(4) returns 4 * 6 = 24, facto(5) returns 5 * 24 = 120


def facto(n):
 if n == 0:
  return 1
 return n * facto (n-1)
print ("Facto of 5:",facto(5))

# Function with keyword arguments
def introduce (name,age):
 print(f"My name is {name} and I am {age} years old")
introduce(name="Valeed", age=30)  

#Passing a List as an Argument

def print_list(items):
 for i in items:
  print(i)
my_list=(10,20,30,40,50,60)
print_list(my_list)

# Positional-Only Arguments
def divide(a,b,/):
 return a/b
print(divide (100,20))  #print(divide (a=100,b=20)) - Error

#Keyword-Only Arguments
def greet(*,name,msg):
 print(f"Hi {name}, {msg}" )
greet(name="Muhammed", msg="How are you?")

#Combine Positional-Only and Keyword-Only
def combo(a,b,/,*,c,d):
 print(a,b,c,d)
combo(1,2,c=3,d=4)

# Using built-in module (math)
import math

print("Square root of 25: ",math.sqrt(25))
print("Value of pi: ", math.pi)
print(math.factorial(7))

#Using built-in module (random)
import random
print("Random number between 1 and 10: ",random.randint(1,10))
print("random choice:",random.choice(["Muhammed","apple","Valeed","banana","cherry"]))
