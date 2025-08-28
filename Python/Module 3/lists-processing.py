#Two lists having the same memory - copying the lists name
list_1 = [2]
list_2 = list_1     #copies the list name, not its content. now two lists have the same memory location, therefor list_2 will have the same value
list_1[0] = 7       #list_2 will change too
print("List 1: ", list_1, "; List 2: ", list_2)
print()

#Copying list content 
#Copying the entire list - list[:]
copy = [1,2,3,4,5]
new_copy1 = copy[:]
print("List copied: ", copy)

#Copying parts of the list (slicing) - list[start_pos : end_pos-1]
new_copy2 = copy[1 : 4]
print("List copied from 2nd to 4th element: ", new_copy2)

#Slicing - negative indices
#1
new_copy3 = copy[2 : -1]
print("List copied from 3rd to 4th element: ", new_copy3)
#2
new_copy4 = copy[-1 : 1]    #starting from the end will print an empty list
print("List copied from the last position to the first: ", new_copy4)

#Slicing - no start position
new_copy5 = copy[:3]
print("List copied from start to 3rd element: ", new_copy5)

#Slicing - no end position
new_copy6 = copy[1:]
print("List copied from the second element to the last: ", new_copy6)

#Slicing - deleting
del copy[3:5]
print("Deleted element 4 and 5: ", copy)
del copy[:]
print("Deleted entire list: ", copy)
print()

#in and not in operators - boolean result
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
