import random

## Single game simulation ##
print("---SINGLE GAME SIMULATION---")

#set up doors, place prize in random door
doors = [1, 2, 3]
prize = random.choice(doors)

#set up doors with no prizes
doors_no_prize = [1, 2, 3]
doors_no_prize.remove(prize)

#choose a random door
choice1 = random.choice(doors)

#reveal a random non-prize door, remove it as a choice if player switches doors
#but do not reveal the door if it was picked
reveal = random.choice(doors_no_prize)
if reveal == choice1:
    while reveal == choice1:
        reveal = random.choice(doors_no_prize)
doors.remove(reveal)

#make a second choice, either switching or staying
choice2 = random.choice(doors)

#did we switch doors or stay with our original door?
if choice1 == choice2:
    action = "Stay"
else:
    action = "Switch"

#did we end up with the right door?
if choice2 == prize:
    win = "Yes!"
else:
    win = "No..."

#print information
print("First choice: Door", choice1)
print("Prize isn't in: Door", reveal)
print("Second choice: Door", choice2)
print("Action:", action)
print("Prize is in: Door", prize)
print("Did we win?", win)


## Multi-game simulation ##
print("\n---MULTI GAME SIMULATION---")
trials = 10000

#Always Stay
stay_wins = 0
for i in range(trials):
    doors = [1, 2, 3]
    prize = random.choice(doors)
    choice1 = random.choice(doors)

    #Since the first choice is what we stick with, the reveal has no effect
    #so just see if the first choice was correct or not.

    if choice1 == prize:
        stay_wins += 1

#Always Switch
switch_wins = 0
for i in range(trials):
    #set up doors
    doors = [1, 2, 3]
    prize = random.choice(doors)
    doors_no_prize = [1, 2, 3]
    doors_no_prize.remove(prize)

    #make choice, set reveal
    choice1 = random.choice(doors)

    reveal = random.choice(doors_no_prize)
    if reveal == choice1:
        while reveal == choice1:
            reveal = random.choice(doors_no_prize)
    doors.remove(reveal)

    #make a second choice that's different from the first choice
    choice2 = random.choice(doors)
    if choice1 == choice2:
        while choice1 == choice2:
            choice2 = random.choice(doors)

    #did we win? if so, add one to the win counter
    if choice2 == prize:
        switch_wins += 1

#Results: number of trials, number of wins, and percent wins rounded to 2 decimals
print("Trials:", trials, "\n")

print("Stay wins:", stay_wins)
stay_success = (stay_wins / trials) * 100
print("Stay success rate:", '%.2f' % stay_success, "%\n")

print("Switch wins:", switch_wins)
switch_success = (switch_wins / trials) * 100
print("Switch success rate:", '%.2f' % switch_success, "%")
