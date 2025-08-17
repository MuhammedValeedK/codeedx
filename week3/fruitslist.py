fruits = ["Banana","Apple", "Jackfruit", "Pineapple", "Watermelon"]

# Create a list of fruits and print each item using a loop

for i in fruits:
    print(i)


#Find the length of a list

length = len(fruits)
print(length)

#Add, remove, and replace elements in a list

fruits.append("Mango")
print(fruits)

fruits.remove("Apple")
print(fruits)

fruits[1] = "Orange"
print(fruits)

fruits.insert(2, "Guava")
print(fruits)

#Sort and reverse a list

list = [34, 56, 12, 78, 90, 45, 67, 89, 23]

list.sort()
print(list)

list.reverse()
print(list)

#Find the largest and smallest number in a list
largest = max(list)
smallest = min(list)

print("Largest number is:", largest)
print("Smallest number is:", smallest)

list.sort()
print("Second largest number is:",list[-2])

# Remove all even numbers from a list.

for i in list:
    if i % 2 == 0:
        print(i,end=" ")
        list.remove(i)

print("new_list =",list)


