"""
https://www.pythoncheatsheet.org/cheatsheet/
Some basics:
1. Variables
2. Flow Controll (if/elif/else)
3. Random
4. Lists
5. Loops
6. Dictionaries
7. String Manipulations
8. Functions
"""


# [1]===========================================================================
import random
time_left = 0.1253432
passed_on_time = True

location_name = "Catacombs F4"
location_text = 'You\'re here:\t\'' + location_name + '\''

score = 98769785975
score_text = "You've earned:\t" + str(score) + " points."

health = 17
MAX_HEALTH = 125
health_lost_text = f'You\'ve lost:\t{MAX_HEALTH - health} health points.\n'


# [2]===========================================================================
if passed_on_time:
    print("Congrats! You've passed the level!")
    print('\t' + score_text + '\n\t' + location_text + '\n\t' + health_lost_text)
elif "F4" in location_name:
    print("Ahh soo close, good luck next time.")
else:
    print("Try again.")


# [3]===========================================================================
hit = random.randint(10, 165)
roll = random.randint(1, 6)
roll_text = f"You have rolled: [{roll}]."
dmg_multiplier = [2.0, 1.5, 1.1, 0.75]
print(roll_text)

if roll == 6:
    dmg = hit * dmg_multiplier[0]
    print(f"{hit} * {dmg_multiplier[0]} =  {dmg}")
    print(f"Excellent! Critical hit! You hit for {dmg}.")

elif roll <= 5 and roll >= 3:
    dmg = hit * dmg_multiplier[1]
    print(f"{hit} * {dmg_multiplier[1]} =  {dmg}")
    print(f"Nice! Critical hit! You hit for {dmg}.")

elif roll == 2:
    dmg = hit * dmg_multiplier[2]
    print(f"{hit} * {dmg_multiplier[2]} =  {dmg}")
    print(f"Good! You hit for {dmg}.")

else:
    dmg = hit * dmg_multiplier[3]
    print(f"{hit} * {dmg_multiplier[3]} =  {dmg}")
    print(f"Better luck next time. You hit for {dmg}.")


# [4]===========================================================================
weapons = ["Sword", "Wand", "Axe", "Zweihänder"]
potions = ["Armor Potion", "Health Potion", "Courage Potion"]
other = []
eq = [weapons, potions, other]

print("Your inventory:")
print(eq)
print(f"You have {len(eq[0]) + len(eq[1]) + len(eq[2])} items.")

print("\nYou have found a treasure!")
treausre = ["Gold Ornament", "Magic Sword"]
other.append(treausre[0])
weapons.insert(2, treausre[1])

print(eq)
print(f"You have {len(eq[0]) + len(eq[1]) + len(eq[2])} items.")

item_used = potions[random.randint(0, len(potions) - 1)]
print(f"\nYou have used {item_used}!")
potions.remove(item_used)

print(eq)
print(f"You have {len(eq[0]) + len(eq[1]) + len(eq[2])} items.")

# [5]===========================================================================
print("\nVillage")
types_of_villagers = ["Townsperson", "Miner", "Guard", "Nobleman"]
population_limit = 100
village_population = []

for i in range(population_limit):
    r_villager_type = random.randint(0, len(types_of_villagers) - 1)
    village_population.append(types_of_villagers[r_villager_type])

for villager in types_of_villagers:
    print(f"{villager.upper()} = [{village_population.count(villager)}]")
print(f"Total: [{len(village_population)}]")

# [6]===========================================================================
quests = {"Yorick's Journal":1060,
          "Grand Tournament":5400,
          "Getting Stronger":640}

print(f"\nYour missions: ")
for name, xp in quests.items():
    print(f"Quests Name: {name}\t Quests XP: {xp}")
    
completed_quest = "Yorick's Journal"
print(f"\nYou have completed {completed_quest} for {quests.get(completed_quest)}xp.\n")

quests.pop(completed_quest)

print(f"Your missions: ")
for name, xp in quests.items():
    print(f"Quests Name: {name}\t Quests XP: {xp}")
    
# [7]===========================================================================
# TODO
# [8]===========================================================================
# TODO

""" console:
Congrats! You've passed the level!
        You've earned:  98769785975 points.
        You're here:    'Catacombs F4'
        You've lost:    108 health points.

You have rolled: [1].
131 * 0.75 =  98.25
Better luck next time. You hit for 98.25.
Your inventory:
[['Sword', 'Wand', 'Axe', 'Zweihänder'], ['Armor Potion', 'Health Potion', 'Courage Potion'], []]
You have 7 items.

You have found a treasure!
[['Sword', 'Wand', 'Magic Sword', 'Axe', 'Zweihänder'], ['Armor Potion', 'Health Potion', 'Courage Potion'], ['Gold Ornament']]
You have 9 items.

You have used Armor Potion!
[['Sword', 'Wand', 'Magic Sword', 'Axe', 'Zweihänder'], ['Health Potion', 'Courage Potion'], ['Gold Ornament']]
You have 8 items.

Village
TOWNSPERSON = [27]
MINER = [24]
GUARD = [28]
NOBLEMAN = [21]
Total: [100]

Your missions:
Quests Name: Yorick's Journal    Quests XP: 1060
Quests Name: Grand Tournament    Quests XP: 5400
Quests Name: Getting Stronger    Quests XP: 640

You have completed Yorick's Journal for 5400xp.

Your missions:
Quests Name: Grand Tournament    Quests XP: 5400
Quests Name: Getting Stronger    Quests XP: 640
"""