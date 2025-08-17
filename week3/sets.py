my_set = {2,3,7,3,4,2,5,4,5,6,7,8}
print(my_set)

my_set2 = {5,6,7,8,9,10,11,12,13,4,5,2}


#union
union_set = my_set.union(my_set2)
print(union_set)

#intersection
print(my_set.intersection(my_set2))


#difference
print(my_set.difference(my_set2))


# Find common elements in three sets.
my_set3 ={14,15,2,3,4}
print(my_set.intersection(my_set2,my_set3))

# Check if two lists have any common elements using sets
list1 = [1,3,5,7,9,2,4,6]
list2 = [2,4,6,8,10,12,14]

set_list1 = set(list1)
set_list2 = set(list2)
 
print(set_list1.intersection(set_list2))