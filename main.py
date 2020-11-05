###RANDOM GAME GENERATOR
#
#
#
import random

gamelimp = []
with open('gamelist.txt', 'r') as rf:
    for line in rf:
        stripline = line.split()
        gamelimp.append(stripline)

print(gamelimp)
gamelimp1 = gamelimp.pop(0)

gamel = ['']
while True:
    gameinput = input('Please input your game list! Type none to break')
    if gameinput == 'none':
        break
    for elem in gamelimp1:
        if elem == gameinput:
            print('You input a duplicate game!')
    else:
        gamel.append(gameinput)

with open('gamelist.txt', 'a+') as f:
    gamestr = ' '.join(gamel)
    f.write(gamestr)
    print(f.read())


# class Games:
#
#     def __init__(self, game, gamenum):
#         self.game = game
#         self.gamenum = gamenum
def randomgen():
    randn = round(random.uniform(1, len(gamelimp1)))
    print(gamelimp1[randn])

randomgen()
