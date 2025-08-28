#   Scenario: A boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
#   Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
#   Note: the height is measured by the number of fully completed layers. e.g. 3 layers, height = 3. even if there are left over blocks

#   Objectives: Familiarize the student with:
#   using the while loop;
#   converting verbally defined loops into actual Python code.

blocks = int(input("Enter the number of blocks: "))
height = 0
counter = 0

while (blocks > 0):
    counter += 1
    blocks -= counter
    if (blocks > 0):
        height += 1
    else:
        break
    
print("The height of the pyramid:", height)

# Explanation: 
# we're decrementing blocks until it a complete pyramid is made, using up the blocks
# a counter is used to count the layers and also increment the amount of blocks that should be used per layer, subtracting it from the blocks
# if there are blocks still available after decrementing for that layer, we increment the height to show a complete layer.