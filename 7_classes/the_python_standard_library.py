# 9.13 - Dice
from random import randint, choices

class Die:
    """A class that represent a dice."""

    def __init__(self, sides=6):
        """Initialize attributes to represent a dice."""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of sides the die has."""
        result = randint(1, self.sides)
        print(f"The result is: {result}")

print("---6 Sides---")
my_die = Die()
for time in range(10):
    my_die.roll_die()

print("---10 Sides---")
my_die = Die(10)
for time in range(10):
    my_die.roll_die()

print("---20 Sides---")
my_die = Die(20)
for time in range(10):
    my_die.roll_die()

# 9.14 - Lottery
lottery_combination = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')
winning_ticket = choices(lottery_combination, k=4)

print("---Winning Ticket---")
print(winning_ticket)

# 9.15 - Lottery Analysis
my_ticket = [0, 8, 2, 1]
times = 0

while True:
    winning_ticket = choices(lottery_combination, k=4)
    times += 1

    if my_ticket == winning_ticket:
        print(f"The Winning Tickets is '{winning_ticket}''")
        print("Congratulations, you won!")
        break
print(f"The numbers of attempts: {times}")
