my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Write a program which removes all the number repetitions from the list. 
# The goal is to have a list in which all the numbers appear not more than once.
# Hint: we encourage you to create a new list as a temporary work area - you don't need to update the list in situ.
new_list = []
for i in my_list:
    if (i not in new_list):
        new_list.append(i)
        
my_list = new_list

print("The list with unique elements only:")
print(my_list)