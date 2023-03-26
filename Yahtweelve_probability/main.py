import random

def convertToDuoDecimal(number):
    if number == 0:
        return 0
    
    digits = []
    while number:
        if number % 12 < 10:
            digits.append(str(number % 12))
        else:
            aAndb = ['a', 'b']
            digits.append(aAndb[number % 12 - 10])
        number //= 12
        
    return ''.join(digits[::-1])
    
def determineCategories(roll_sequence):
    categories = []
    roll = [int(figure, 12) for figure in list(roll_sequence)]
    unique_roll = list(set(sorted(roll)))
    
    if len([1 for pips in roll if (roll.count(pips) == 3)]) == 3: #Three of a kind
        categories.append(0)
        
    if len([1 for pips in roll if (roll.count(pips) == 4)]) == 4: #Four of a kind
        categories.append(1)
        
    if sum(roll) <= 20: #Sub twenty
        categories.append(2)
        
    if sum(roll) <= 15: #Sub fourty
        categories.append(3)
        
    if len([1 for i, pips in enumerate(unique_roll) if pips - 1 == unique_roll[i - 1]]) >= 3: #Small street
        categories.append(4)
        
    if len([1 for n in [2,3] if n in [roll.count(pips) for pips in roll]]) == 2: #Full house
        categories.append(5)
        
    if len([1 for i, pips in enumerate(unique_roll) if pips - 1 == unique_roll[i - 1]]) >= 4: #Large street
        categories.append(6)
        
    if len(unique_roll) == 1: #Yahtweelve
        categories.append(7)
    
    return categories

###Calculate hold_posibilities
hold_posibilities = []
for i in range(32): #2**5
    hold_string = bin(i)[2:].zfill(5)
    hold_posibilities.append(hold_string)
    
print('Hold posibilities:', len(hold_posibilities))

###Predict à la Monte Carlo
ITTERATIONS = 10000

category_counts = [0]*8
for i in range(ITTERATIONS):
    roll = []
    for die_number in range(5):
        roll.append(convertToDuoDecimal(random.randint(1,12)))
    
    #######NEED TO ADD SECOND AND THIRD STAGE!!!
    
    categories = determineCategories(roll)
    
    for category in categories:
        category_counts[category] += 1
        
print(category_counts)

"""
###Calculate roll posibilities WIP
roll_possibilies = []
for i in range(248831): #12 ** 5 - 1
    dice_string = convertToDuoDecimal(i+1).zfill(5)
    roll_possibilies.append(dice_string)

print('Roll posibilities:', len(roll_possibilies))
"""