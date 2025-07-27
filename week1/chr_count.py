#.Length of a String

name = input("Enter your name: ")
count = len(name)
print(f"Your name has {count} characters")

#Age Comparison 

age1 = int(input("Enter your age: "))
age2 = int(input("Enter your friend's age: "))

if age1 > age2:
    print("You are older than your friend.")
elif age1 < age2:
    print("You are younger than your friend.")
else:
    print("You are the same age as your friend.")