#Creating and assigning a list
numbers = [7,9,5,2,4]
print("Original list: ", numbers)
print()

#Accessing indexes (positive and negative indices) and the length of the list
print("numbers[1]: ", numbers[1])   #forward
print("numbers[-1]", numbers[-1])  #backwards
print("Length of the list: ", len(numbers))
print()

#Changing a value in the list
numbers[0] = 6
print("Updated list: ", numbers)
print()

#Deleting a value in the list
del numbers[4]
print("Updated list: ", numbers)
print("Length of the updated list: ", len(numbers))
print()

#Asking a user to enter a number to replace
num_replace = int(input("Enter a number to replace the third element: "))
numbers[2] = num_replace
print()

