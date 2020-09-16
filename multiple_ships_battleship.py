# currently working on this file
from random import randint

def print_board(board):
  for row in board:
    print (" ".join(row))

def random_row():
  return randint(0, 9)

def random_col():
  return randint(0, 9)

def ship_dir():
  return randint(0,3)

ship_sizes = [2,3,3,4,5]

# ship_row
# ship_col
# ship_direction
# ship_size 

# creating a ship array with all places to guess
full_ship = []
ship_being_created = []

print("program good till basic")

# make a def check_any_ships_nearby use in repetative for loop of def ship_dir_inc
# def check_any_ships_nearby(ship_row,ship_col,ship_size):
#     i=0
#     if ship_dir == 0:
#         for i in range(ship_size):
#             ship_being_created.append(ship_row,ship_col+i)

# create a function that sees two or three steps ahead of the ship use func above
# create by using a list of ship created two for loops check:
# for a in ship_being created:
#   for b in full_ship:
#       if a[0] == b[0] and a[1] == b[1]:
#           ship_sizes.append(ship_size)
#           creating_full_ship()

# let check function only check first then append else dont : kind of AI looks forward

# for ship in ship_being_created:
#   full_ship.append(ship)

# while ship_being_created not equal None:
#   for x in ship_being_created:
#       ship_being_created.remove(x)

def pop_list(mylist,size):
    for x in range(size):
        mylist.pop()

def check_any_ships_nearby(ship_row,ship_col,ship_size):
    # for i in full_ship:
    #     if i[0] == ship_row and i[1] == ship_col:
    #         print("Sorry error occured this location is already taken")
    #         print("on position" , i)
    #         break

    # maybe change loops try something new
    print(ship_being_created)
    for a in ship_being_created:
        for b in full_ship:
            if a[0] == b[0] and a[1] == b[1]:
                print("Sorry error occured this location is already taken")
                print("on position" , a)
                # f = len(ship_being_created)
                ship_sizes.append(ship_size)
                pop_list(full_ship,ship_size)
                break
                # creating_full_ship_list()
            else:
                continue
    # for ship in ship_being_created:
    #     full_ship.append(ship)
    full_ship.extend(ship_being_created)
    # while bool(ship_being_created) == True:
    # for x in ship_being_created:
    #     ship_being_created.remove(x)
    ship_being_created.clear()


def ship_dir_inc(ship_row,ship_col,ship_direction,ship_size):
    print("inside ship_dir_inc")
    ship_inc = 1
    ship_dec = 0
    for x in range(ship_size):
        if ship_direction == 1:
            if ship_row-ship_dec < 0:
                check_any_ships_nearby(ship_row+ship_inc , ship_col, ship_size)
                ap1 = (ship_row+ship_inc , ship_col)
                # full_ship.append(ap1)
                ship_being_created.append(ap1)
                ship_inc += 1
            else:
                check_any_ships_nearby(ship_row-ship_dec , ship_col, ship_size)
                ap2 = (ship_row-ship_dec , ship_col)
                # full_ship.append(ap2)
                ship_being_created.append(ap2)
                ship_dec += 1

        elif ship_direction == 3:
            if ship_row + ship_inc > 9:
                check_any_ships_nearby(ship_row-ship_dec , ship_col, ship_size)
                ap3 = (ship_row-ship_dec , ship_col)
                # full_ship.append(ap3)
                ship_being_created.append(ap3)
                ship_dec += 1
            else:
                check_any_ships_nearby(ship_row+ship_inc , ship_col, ship_size)
                ap4 = (ship_row+ship_inc , ship_col)
                # full_ship.append(ap4)
                ship_being_created.append(ap4)
                ship_inc +=1

        elif ship_direction == 2:
            if ship_col-ship_dec < 0:
                check_any_ships_nearby(ship_row , ship_col+ship_inc, ship_size)
                ap5 = (ship_row , ship_col+ship_inc)
                # full_ship.append(ap5)
                ship_being_created.append(ap5)
                ship_inc += 1
            else:
                check_any_ships_nearby(ship_row , ship_col-ship_dec, ship_size)
                ap6 = (ship_row , ship_col-ship_dec)
                # full_ship.append(ap6)
                ship_being_created.append(ap6)
                ship_dec += 1
        
        elif ship_direction == 0:
            if ship_col+ship_inc > 9:
                check_any_ships_nearby(ship_row , ship_col-ship_dec, ship_size)
                ap7 = (ship_row , ship_col-ship_dec)
                # full_ship.append(ap7)
                ship_being_created.append(ap7)
                ship_dec += 1
            else:
                check_any_ships_nearby(ship_row , ship_col+ship_inc, ship_size)
                ap8 = (ship_row , ship_col+ship_inc)
                # full_ship.append(ap8)
                ship_being_created.append(ap8)
                ship_inc += 1

def creating_full_ship_list():
    print("inside creating_full_ship_list")
    for ship in ship_sizes:
        ships_row = random_row()
        ships_col = random_col()
        ships_direction = ship_dir()
        ship_dir_inc(ships_row,ships_col,ships_direction,ship)

creating_full_ship_list()
print(full_ship)
print(ship_being_created)

guess_board = []

for i in range(9):
  guess_board.append(["0"] * 9)

print_board(guess_board)