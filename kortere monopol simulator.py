from random import randint

brett = {
    1: ('brun', 0),
    3: ('brun', 1),
    6: ('lyseblaa', 0),
    8: ('lyseblaa', 1),
    9: ('lyseblaa', 2),
    11: ('rosa', 0),
    13: ('rosa', 1),
    14: ('rosa', 2),
    16: ('oransj', 0),
    18: ('oransj', 1),
    19: ('oransj', 2),
    21: ('rod', 0),
    23: ('rod', 1),
    24: ('rod', 2),
    26: ('gul', 0),
    27: ('gul', 1),
    29: ('gul', 2),
    31: ('grønn', 0),
    32: ('grønn', 1),
    34: ('grønn', 2),
    37: ('blaa', 0),
    39: ('blaa', 1),
}

steder = {
    'brun': [0, 0],
    'lyseblaa': [0, 0, 0],
    'rosa': [0, 0, 0],
    'oransj': [0, 0, 0],
    'rod': [0, 0, 0],
    'gul': [0, 0, 0],
    'grønn': [0, 0, 0],
    'blaa': [0, 0, 0]
}

brikke = 0
fengsel = 0
iteration = 0

num = int(input("hvor mange kast vil du simulere? "))
for h in range(num):
    brikke += randint(1, 6) + randint(1, 6)

    if brikke > 40:
        brikke -= 40
        iteration += 1

    if brikke == 30:
        brikke = 10
        fengsel += 1

    house_set, plasering = brett.get(brikke, (None, None))
    if house_set is not None:
        steder[house_set][plasering] += 1

totals = {plasering: sum(house_set) for plasering, house_set in steder.items()}

for plasering, amount in totals.items():
    print('{} = {}'.format(plasering, amount))

for plasering, house_set in steder.items():
    for i, amount in enumerate(house_set, 1):
        print('{} {} = {}'.format(plasering, i, amount))

print("Du kom i fengsel %d ganger" %(fengsel))

digit = len(str(max(amount for house_set in steder.values() for amount in house_set)))
blank = "-" * digit
space = " " * digit
plaserings_format = '{{:0>{}}}'.format(digit)

formatted = {
    plasering: [plaserings_format.format(amount) for amount in house_set]
    for plasering, house_set in steder.items()
}

brettkant = []
for index in range(40):
    plasering = brett.get(index, None)
    if plasering is None:
        value = blank
    else:
        value = steder[plasering[0]][plasering[1]]
    brettkant.append(value)
brettkant[0] = 'Go'

brett = [[space] * 11 for _ in range(11)]
for index in range(40):
    x, y = 0, 0
    if index < 11:
        x = 10 - index
        y = 10
    elif index < 21:
        x = 0
        y = 10 - (index - 10)
    elif index < 31:
        x = index - 20
    else:
        x = 10
        y = index - 30
    brett[y][x] = brettkant[index]

for line in brett:
    print('  {}  '.format('  |  '.join(str(p) for p in line)))