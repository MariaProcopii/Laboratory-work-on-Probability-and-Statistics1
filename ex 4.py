import random

def game21(n, k, maxpts):
    nrOfGames = 10000000
    win = 0
    for _ in range(nrOfGames):
        points = 0
        while(points < k):
            points += random.randint(1, maxpts)
        if(points <= n):
            win += 1
    return win / nrOfGames


print(game21(10, 1, 10))
print(game21(6, 1, 10))
print(game21(21, 17, 10))


