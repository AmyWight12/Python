#   Scenario: There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
#   Objectives: Familiarize the student with
#   - using basic instructions related to lists;
#   - creating and modifying lists.

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
replace_num = int(input("Enter a number that will replace the middle number in the list: "))
hat_list[2] = replace_num

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]

# Step 3: write a line of code that prints the length of the existing list.
print("Length of the altered list: ", len(hat_list))

print(hat_list)
