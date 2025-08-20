#Syntax:  the name of the desired variable, then the equal sign (=) and the value you want to put into the variable.
#You're not allowed to use a variable which doesn't exist (in other words, a variable that was not assigned a value).

#Simple:
var = 36
print(var)
print()

#Printing multiple variables:
var = 32
acc_balance = 1800.50
client_name = 'Amy'
print(var, acc_balance, client_name)
print()

#Combining text and variables:
var = "3.8.5"
print("Python version: " + var)
print()

#Assigning a new value to an already existing variable (incrementing):
var = 5
print(var)
var = var + 2
print(var)
print()

#Simple maths problems:
a = 4.0
b = 2.0
c = (a**2 + b**3) * 0.5
print("c= ", c)
print()

#Shorcut for incrementing/decrementing:
var = 6
print("Original var: ", var)
var = var + 2
print("Long way of incrementing: ", var)
var = 6
var += 2
print("Shortcut of incrementing: ", var)
