import math
import random
from math import log2

maxMoney = int(input())

def payment(a):
    nrofwin = math.log2(a)
    willpay = round(nrofwin, 3)
    return f'The amount you are willing to pay is {willpay}$'

print(payment(maxMoney))


# import random
#
# def game(nrgames):
# 	willingToPay = 0
# 	win = 0
# 	for i in range(nrgames):
# 		toss = random.randint(0, 1)
# 		while (toss == True):
# 			win += 1
# 			toss = random.randint(0, 1)
# 		willingToPay += 2**(win)
# 		win = 0
# 	return (willingToPay)
#
# print(game(100),'$')