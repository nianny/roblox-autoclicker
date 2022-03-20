import random

class Passenger:
  row: int
  col: int
  luggage: int

  def __init__(self, row: int, col: int, luggage: int):
    self.row = row
    self.col = col
    self.luggage = luggage
  
  def __repr__(self):
    return f"(row: {self.row}, col: {self.col}, luggage: {self.luggage})"

SEED: int = 20220315
ROWS: int = 20
COLS: int = 3

MAX_LUGGAGE: int = 3

random.seed(SEED)


walkway: list[Passenger] = [None for _ in range(ROWS)]

seats: list[Passenger] = [[None for _ in range(COLS * 2)] for _ in range(ROWS)]

passengers: list[Passenger] = []

for r in range(ROWS):
  for c in range(COLS):
    passengers.append(Passenger(r, c, random.randrange(0, MAX_LUGGAGE)))

random.shuffle(passengers)

done: bool = False #set to true then to false if any passenger

walksteps: int = 0
stowsteps: int = 0
sitsteps: int = 0
steps: int = 0

while not done:
  steps += 1

  done = True

  for r in reversed(range(ROWS)):
    p = walkway[r]

    if not p:
      continue
    
    if p.row == r:
      if p.luggage:
        p.luggage -= 1
        done = False
      else:
        seats[p.row][p.col] = p
        walkway[r] = None
    elif not walkway[r + 1]:
      walkway[r + 1] = p
      walkway[r] = None
      done = False
  
  if passengers and not walkway[0]:
    walkway[0] = passengers.pop()
    done = False

  print(f"Step: {steps}\n")

  for c in range(COLS):
    for r in range(ROWS):
      if seats[r][c]:
        print("0", end = "")
      else:
        print("e", end = "")
    print()
  print()

  for r in range(ROWS):
    if not walkway[r]:
      print(" ", end = "")
    elif walkway[r].row == r:
      print(walkway[r].luggage, end = "")
    else:
      print("w", end = "")
  print("\n")

  for c in range(COLS, COLS * 2):
    for r in range(ROWS):
      if seats[r][c]:
        print("0", end = "")
      else:
        print("e", end = "")
    print()
  print("-" * ROWS)

  input("Press ENTER to continue")

print(f"Steps taken: {steps}")