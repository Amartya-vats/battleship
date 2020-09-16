from random import randint

def print_board(board):
  for row in board:
    print (" ".join(row))


def random_row():
  return randint(0, 4)

def random_col():
  return randint(0, 4)

ship_row = random_row()
ship_col = random_col()

def ship_dir():
  return randint(0,3)

ship_direction = ship_dir()
# print(ship_direction)
ship_inc = 1
ship_dec = 1

# board[ship_row][ship_col] = "s"
full_ship = [(ship_row,ship_col)]

for x in range(2):
  if ship_direction == 1:
    if ship_row - ship_dec < 0: #ship_row + ship_direction > 4 or 
      # board[ship_row + ship_inc][ship_col] = "s"
      ap1 = (ship_row+ship_inc , ship_col)
      full_ship.append(ap1)
      ship_inc += 1
    else:
      # board[ship_row - ship_dec][ship_col] = "s"
      ap2 = (ship_row - ship_dec , ship_col)
      full_ship.append(ap2)
      ship_dec += 1

  elif ship_direction == 3:
    if ship_row + ship_inc > 4:
      # board[ship_row - ship_dec][ship_col] = "s"
      ap3 = (ship_row - ship_dec , ship_col)
      full_ship.append(ap3)
      ship_dec += 1
    else:
      # board[ship_row + ship_inc][ship_col] = "s"
      ap4 = (ship_row+ship_inc , ship_col)
      full_ship.append(ap4)
      ship_inc +=1

  elif ship_direction == 2:
    if ship_col - ship_dec < 0:
      # board[ship_row][ship_col + ship_inc] = "s"
      ap5 = (ship_row , ship_col+ship_inc)
      full_ship.append(ap5)
      ship_inc += 1
    else:
      # board[ship_row][ship_col - ship_dec] = "s"
      ap6 = (ship_row , ship_col-ship_dec)
      full_ship.append(ap6)
      ship_dec += 1
  
  elif ship_direction == 0:
    if ship_col + ship_inc > 4:
      # board[ship_row][ship_col - ship_dec] = "s"
      ap7 = (ship_row , ship_col-ship_dec)
      full_ship.append(ap7)
      ship_dec += 1
    else:
      # board[ship_row][ship_col + ship_inc] = "s"
      ap8 = (ship_row , ship_col+ship_inc)
      full_ship.append(ap8)
      ship_inc += 1

# print_board(board)

# print(full_ship)
# creating a guess_board
guess_board = []

for i in range(5):
  guess_board.append(["0"] * 5)

print_board(guess_board)

print("Now you can start guessing. ")
print ("Please keep in mind that the number of rows and columns starts from 0. ")
print("Ship size is 3. ")
print("Guess accordingly. ")
turn = 1
while True:
  print("Guess Row: ")
  guess_row = int(input())
  print ("Guess Col: ")
  guess_col = int(input())
  print ("Turn", turn)
  if (guess_col > 4 or guess_row > 4 or guess_col<0 or guess_row<0):
    print ("Your guess was outside the board")
    # print("Guess Row: ")
    # guess_row = int(input())
    # print ("Guess Col: ")
    # guess_col = int(input())
    continue
  else:
    if (len(full_ship) == 1):
      guess_board[guess_row][guess_col] = "H"
      print_board(guess_board)
      print ("Total number of turns:", turn)
      # print(turn)
      print("Congratulations you have sunk my ship")
      break
    else:
      for i in full_ship:
        if i[0] == guess_row and i[1] == guess_col:
          print("You have a hit")
          guess_board[guess_row][guess_col] = "H"
          full_ship.remove(i)
          break
        else:
          guess_board[guess_row][guess_col] = "X"
      if guess_board[guess_row][guess_col] == "X":
        print("You Missed")
      print_board(guess_board)
      turn += 1