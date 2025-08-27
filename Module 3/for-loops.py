#basic structure - range() with one argument
#for loop starts at 0
for i in range(5):
    print("The value of i is: ", i)     #range is 0-4
print()

#range() with two arguments - start and end value
for j in range(2,6):
    print("The value of j is: ", j)     #actual end value is 5 (end_value - 1), so the range is 2-5
print()

#range() with three arguments - start value, end value, increment value
for k in range(2,8,3):
    print("The value of k is: ", k)     #post increments, actual end value is 7: range is 2-7 incrementing by 3 after each iteration until the end value is reached
print()

#break statement - we want to skip the 3rd iteration
for i in range(1,6):
    if i == 3:
        break                           #exits the entire for loop so 4,5,6 won't be printed
    print("Inside the loop. ", i)       #continuation of loop (next instruction)
print("Outside the loop.")              #break executes the nearest instruction immediately.
print()

#continue statement - we want to skip the 3rd iteration
for j in range(1,6):
    if j == 3:
        continue                        #skips the current iteration and continues with the loop
    print("Inside the loop. ", j)       #continuation of loop (next instruction)
print("Outside of the loop.")
print()