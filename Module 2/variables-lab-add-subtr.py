#Lab: John had three apples, Mary had five apples, and Adam had six apples.
#create the variables: john, mary, and adam;
#assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
#having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
#now create a new variable named total_apples equal to addition of the three former variables.
#print the value stored in total_apples to the console;

john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=", ")
total_apples = john + mary + adam
print("Total apples: ", total_apples)