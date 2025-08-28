#creating a room booking system. 3 hotels, 15 floors, 20 rooms

rooms = [[[False for i in range(20)] for i in range(15)] for i in range(3)]
# inner loop is for the rooms
# middle loop if for the floors
# outer loop is for the hotel buildings

rooms[2][9][17] = True
# the 18th room, on the 10th floor, in the 3rd hotel is booked