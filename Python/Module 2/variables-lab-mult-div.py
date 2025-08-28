#Lab: Miles and kilometers are units of length or distance.
#1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts: miles to kilometers; kilometers to miles.
#Do not change anything in the existing code, except for the conversion variables
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")  #round() function rounds the outputted value to the number of decimals specified in the parenthesis
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")