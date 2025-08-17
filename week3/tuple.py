my_tuple = ("apple", "banana", "cherry")

#Create a tuple of colors and access elements using indexing
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])



#Check if an element exists in a tuple
if "apple" in my_tuple:
    print("Yes, 'apple' is in the fruits tuple")


#convert tuple to list
my_list = list(my_tuple)
print(my_list)  


my_tuple =  tuple(my_list)
print(my_tuple)