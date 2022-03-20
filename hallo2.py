import random
import numpy as np




rows = 33
passenger_per_side = 3 
carry_on_max = 3 
carry_on_sum = 100
walk_time = 1
put_in_time = 5
sit_time = 2

lane = [None] * rows
seats = [[None for _ in range(passenger_per_side*2)] for _ in range(rows)]
carry_on = [[random.randint(0, carry_on_max) for p in range(passenger_per_side*2)] for i in range(rows)]

for _ in range(carry_on_sum):
    x,y = random.randint(0, rows-1), random.randint(0, passenger_per_side*2-1)
    while (carry_on[x][y]>carry_on_max):
        continue
    carry_on[x][y] += 1

print(carry_on[x][y])

class Passenger:
    def __init__(self, x, y, bags, pos = None, action_time = None):
        self.x = x
        self.y = y
        self.pos = pos
        self.action_time = action_time
        self.bags = bags

    def execute(self, time):
        # print('funcbefore', time, self.action_time, self.pos, self.x, self.y, self.bags)
        if time != self.action_time:
            return self.action_time
        if (self.pos != None):
            if (self.pos == self.x):
                if self.bags > 0:
                    self.bags -= 1
                    #print(self.action_time)
                    self.action_time += put_in_time
                    #print(self.action_time)
                elif self.bags == 0:
                    self.bags -= 1
                    self.action_time += sit_time
                else:   
                    lane[self.pos] = None
                    self.pos = None
                    seats[self.x][self.y] = self

            elif (lane[self.pos+1] == None):
                self.pos += 1
                self.action_time += 1
                lane[self.pos] = self
                lane[self.pos-1] = None
            else:
                self.action_time += 1

        # print('func after', time, self.action_time, self.x, self.y, self.pos, self.bags)
        return self.action_time
      

passengers = [ Passenger(i,p, carry_on[i][p]) for p in range(passenger_per_side*2) for i in range(rows)]


random.shuffle(passengers)



max_time = 1
time = 0
while time <= max_time:
    for person in reversed(lane):
        if person != None:
            each_time = person.execute(time)
            max_time = max(max_time, each_time)
    
    time += 1
    if len(passengers) > 0 and lane[0] == None:
        lane[0] = passengers[0]
        passengers = passengers[1:]
        lane[0].action_time = time
        lane[0].pos = 0

    for i in range(passenger_per_side):
        for p in range(rows):
            if seats[p][i]:
                print('X', end=' ')
            else:
                print('0', end=' ')
        print()
    for i in lane:
        if i:
            if i.pos == i.x:
                if i.bags >= 0:
                    print(i.bags, end=' ')
                elif i.bags == -1:
                    print('S', end=' ')
            else:
                print('W', end=' ')
        else:
            print(' ', end=' ')
    print()
    for i in range(passenger_per_side):
        for p in range(rows):
            if seats[p][i+3]:
                print('X', end=' ')
            else:
                print('0', end=' ')
        print()
    
    print()
    print()
    
    # input("Press Enter to continue...")
    
    
print(max_time)




