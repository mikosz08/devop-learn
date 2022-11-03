"""
https://www.pythoncheatsheet.org/cheatsheet/
Some basic examples of:
1. Variables
2. Flow Controll (if/elif/else)
3. Random
4. Lists
5. Loops
6. Dictionaries
7. String Manipulations
8. Functions
"""
import random
from re import A
from time import sleep


def line():
    print(f'\n' + '~#' * 35)


# [1]===========================================================================
time_left = 0.1253432

passed_on_time = True
luck = random.random()
if luck > 0.4345765:
    passed_on_time = False

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
hit = random.randint(43, 78)
roll = random.randint(1, 6)
roll_text = f"You have rolled: [{roll}]."
dmg_multiplier = (2.0, 1.5, 1.1, 0.75)
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
population_limit = 10_000
village_population = []

for i in range(population_limit):
    r_villager_type = random.randint(0, len(types_of_villagers) - 1)
    village_population.append(types_of_villagers[r_villager_type])

for villager in types_of_villagers:
    print(f"{villager.upper()} = [{village_population.count(villager)}]")
print(f"Total: [{len(village_population)}]")

# [6]===========================================================================
quests = {"Yorick's Journal": 1060,
          "Grand Tournament": 5400,
          "Getting Stronger": 640}

print(f"\nYour missions: ")
for name, xp in quests.items():
    print(f"Quests Name: {name}\t Quests XP: {xp}")

completed_quest = "Yorick's Journal"
print(
    f"\nYou have completed {completed_quest} for {quests.get(completed_quest)}xp.\n")

deleted_quest = quests.pop(completed_quest)

print(f"Your missions: ")
for name, xp in quests.items():
    print(f"Quests Name: {name}\t Quests XP: {xp}")

# [7]===========================================================================
print()
quote = """
a wizard is never late
frodo Baggins
nor is he early He arrives precisely when he means to
                                            — Gandalf
"""
print(quote + '\n')
quote_words = quote.split()
print(quote_words)
print(f"This quote have {len(quote)} letters, and {len(quote_words)} words.\n")

quote = """
It is the job that is never started as takes longest to finish 
                                                    - Sam Gamgee
Even the smallest person can change the course of the future
                                                    - Galadriel
I would rather share one lifetime with you than face all the ages of this world alone
                                                    - Arwen
"""

words = quote.split()
word_count_dict = {}
counter = 1

for word in words:
    if word in word_count_dict:
        word_count_dict[word] += counter
    else:
        word_count_dict[word] = counter

print("Characters occurances: ")
loops = 5
for w, c in word_count_dict.items():
    if (loops) == 0:
        break
    print(f"Word: '{w}'\nOccured: {c} time/s.\n===")
    loops -= 1

# [8]===========================================================================


def prepare(hp: int, attack: int, bag: list):
    stats = [hp, attack]
    return stats, bag

def fight(player, enemy):
    import random
    roll = random.random()
    player_turn = False
    if roll > 0.50:
        print(f"You attack first! ({roll})")
        player_turn = True
    else:
        print(f"Enemy starts. ({roll})")

    round = 1
    while enemy[0][0] > 0 and player[0][0] > 0:
        print(f"\n================Round {round}================")
        print(f"Player's HP: {player[0][0]}")
        print(f"Enemy's HP: {enemy[0][0]}")
        if player_turn:
            hit = int(player[0][1] * random.random())
            enemy[0][0] -= hit
            print(f"\t Player hits for: {hit}")
            if enemy[0][0] <= 0:
                print(f"Player wins!"); continue
            player_turn = False
        else:
            hit = int(enemy[0][1] * random.random())
            player[0][0] -= hit
            print(f"\t Enemy hits for: {hit}")
            if player[0][0] <= 0:
                print(f"Enemy wins!"); continue
            player_turn = True
        round += 1


player = prepare(hp=15, attack=9, bag=["HP Potion", "Elixir of Swiftness"])
enemy = prepare(hp=10, attack=10, bag=[])

print(f"Player's stats: {player}")
print(f"Enemy's stats: {enemy}")
fight(player, enemy)




""" console:
Congrats! You've passed the level!
        You've earned:  98769785975 points.
        You're here:    'Catacombs F4'
        You've lost:    108 health points.

You have rolled: [1].
78 * 0.75 =  58.5
Better luck next time. You hit for 58.5.
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
TOWNSPERSON = [2475]
MINER = [2511]
GUARD = [2525]
NOBLEMAN = [2489]
Total: [10000]

Your missions:
Quests Name: Yorick's Journal    Quests XP: 1060
Quests Name: Grand Tournament    Quests XP: 5400
Quests Name: Getting Stronger    Quests XP: 640

You have completed Yorick's Journal for 1060xp.

Your missions:
Quests Name: Grand Tournament    Quests XP: 5400
Quests Name: Getting Stronger    Quests XP: 640


a wizard is never late
frodo Baggins
nor is he early He arrives precisely when he means to
                                            — Gandalf


['a', 'wizard', 'is', 'never', 'late', 'frodo', 'Baggins', 'nor', 'is', 'he', 'early', 'He', 'arrives', 'precisely', 'when', 'he', 'means', 'to', '—', 'Gandalf']
This quote have 146 letters, and 20 words.

Characters occurances:
Word: 'It'
Occured: 1 time/s.
===
Word: 'is'
Occured: 2 time/s.
===
Word: 'the'
Occured: 5 time/s.
===
Word: 'job'
Occured: 1 time/s.
===
Word: 'that'
Occured: 1 time/s.
===
Player's stats: ([15, 9], ['HP Potion', 'Elixir of Swiftness'])
Enemy's stats: ([10, 10], [])
You attack first! (0.6492307796601187)

================Round 1================
Player's HP: 15
Enemy's HP: 10
         Player hits for: 3

================Round 2================
Player's HP: 15
Enemy's HP: 7
         Enemy hits for: 7

================Round 3================
Player's HP: 8
Enemy's HP: 7
         Player hits for: 8
Player wins!
"""
