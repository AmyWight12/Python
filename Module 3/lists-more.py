#Creating a list
numbers = [7,9,5,2,4]
print("Original list: ", numbers)
print()

#Adding an element to the end of a list - list.append(value)
numbers.append(0)
print("Appended list: ", numbers)
print("Length of list: ", len(numbers))
print()

#Adding an element anywhere in the list - list.insert(location,value)
numbers.insert(0,33)    #doesn't replace the first element, it shits everything down one
print("Inserted list: ", numbers)
print("Length of list: ", len(numbers))
print()

#Adding elements to an empty list
new_list = []

for i in range(5):  #0-4
    new_list.append(i+1)    #or new_list.insert(0, i+1)
print("New list 1: ", new_list)
print()

#Totaling elements 
total = 0

for i in range(len(numbers)):
    total += numbers[i]
print("Total: ", total)
print()

#Swapping without a loop - reversal order
swap_1 = [10,2,3,5,8]
print("Original list 1: ", swap_1)

swap_1[0], swap_1[4] = swap_1[4], swap_1[0]
swap_1[1], swap_1[3] = swap_1[3], swap_1[1]

print("Reveresed list: ", swap_1)
print()

#Swapping with a loop - reversal order
swap_2 = [4,9,8,5,6]
length = len(swap_2)
print("Original list 2: ", swap_2)

for i in range(length // 2):
    swap_2[i], swap_2[length - i - 1] = swap_2[length - i - 1], swap_2[i]

print("Reversed list 2: ", swap_2)
print()