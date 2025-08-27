# if true_or_not:
#   perform_if_true (indented for true)
# carry_on_with_program (not indented)

# if true_or_not:
#   perform_if_true
# else:
#   perform_if_false
# carry_on_with_program

# if the_weather_is_good:
#     go_for_a_walk()
# elif tickets_are_available:
#     go_to_the_theater()
# elif table_is_available:
#     go_for_lunch()
# else:
#     play_chess_at_home()


#reas two number
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

#find larger number
if (num1 > num2): larger_num = num1
else: larger_num = num2

#print larger number
print("the larger number is: ", larger_num)