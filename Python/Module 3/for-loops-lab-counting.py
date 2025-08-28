#   Scenario: The Mississippi River is about 2,340 miles long, which makes it the second longest river in the United States. A single drop of water needs 90 days to travel its entire length!
#   The word Mississippi is also used for a slightly different purpose: to count mississippily (used to count seconds).
#   Task:
#   1. write a program that uses a for loop to "count mississippily" to five.
#   2. the program should print to the screen the final message "Ready or not, here I come!"
#   3. import time and sleep() is added for you

import time

for i in range(1,6):
    print(i, " Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")