import random

def adjacentBullets(nrOfBullets):
    magazine = [0] * nrOfBullets #magazine with n number of slots barrel
    lastindex = nrOfBullets - 1
    indexbullet1 = random.randint(0, lastindex) #position of first bullet
    indexbullet2 = indexbullet1 + 1
    if(indexbullet2 > lastindex):
        indexbullet2 = 0 # first position in magazine
    magazine[indexbullet1] = 1 # bullet 1 in the magazine
    magazine[indexbullet2] = 1 # bullet 2 in the magazine
    return magazine

def noAdjacentBullets(nrOfBullets):
    magazine = [0] * nrOfBullets
    lastindex = nrOfBullets - 1
    indexbullet1 = random.randint(0, lastindex)
    indexbullet2 = random.randint(0, lastindex)
    while(indexbullet2 == indexbullet1):
        indexbullet2 = random.randint(0, lastindex)
    magazine[indexbullet1] = 1
    magazine[indexbullet2] = 1
    return magazine

def gameoflife(nrGame, nrOfBullets, adjacent):
    deathIfSpin = 0
    aliveIfSpin = 0
    deathNoSpin = 0
    aliveNoSpin = 0
    lastindex = nrOfBullets - 1
    for i in range(nrGame):
        if(adjacent == 'YES'):
            magazine = adjacentBullets(nrOfBullets)
        else:
            magazine = noAdjacentBullets(nrOfBullets)
        spinIndex = random.randint(0, lastindex)
        if(magazine[spinIndex] == 1):
          ...
        else:
            spinIndex += 1 #here we are not spinning. Move index to one
            if(spinIndex > lastindex):
                spinIndex = 0
            if(magazine[spinIndex] == 1):
                deathNoSpin += 1
            else:
                aliveNoSpin += 1

            spinIndex = random.randint(0, lastindex)
            if(magazine[spinIndex] == 1):
                deathIfSpin += 1
            else:
                aliveIfSpin += 1
    print("Chance of death  with spin:", round(deathIfSpin / nrGame * 100, 3), "%")
    print("Chance of staying alive with spin:", round(aliveIfSpin / nrGame * 100, 3), "%")
    print("Chance of death  with no spin:", round(deathNoSpin / nrGame * 100, 3), "%")
    print("Chance of staying alive with no spin:", round(aliveNoSpin / nrGame * 100, 3), "%")

print(gameoflife(100, 9, 'YES'))