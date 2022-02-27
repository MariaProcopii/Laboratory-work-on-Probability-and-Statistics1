import hashlib
import  string
import random


allL = string.ascii_letters
dictH = {}

def randomhash():
    for _ in range((2**int(32/2))):     # byte combination
        randomStr = ''.join(random.choice(allL) for _ in range(10))
        randomStr = randomStr.encode()          # Converts the string into bytes to be acceptable by hash function
        randomStrHash = hashlib.md5(randomStr).hexdigest()     #Returns the encoded data in hexadecimal format
        if(randomStrHash[:10] in dictH):
            print(hashlib.md5(dictH[randomStrHash[:10]]).hexdigest())
            print(randomStrHash)
            return True
        else:
            dictH[randomStrHash[:10]] = randomStr
            return False

collision = False
while(collision == False):
    collision = randomhash()

#print(dictH)

# import hashlib
# import random
#
#
#
# def day():
#     first = random.randint(0, 31)
#     if (first == 0 and first > 31):
#         first = random.randint(0, 31)
#     return first
# R = 3
# dictH = {}
# def randomhash():
#     for _ in range((2**int(32))):     # byte combination
#         month = random.randint(1, 12)
#         year = random.randint(1900, 2003)
#         randomBirthday = f'{day()}.{random.randint(1, 12)}.{random.randint(1900, 2003)}'
#         randomBirthday = randomBirthday.encode()          # Converts the string into bytes to be acceptable by hash function
#         randomBirthdayHash = hashlib.md5(randomBirthday).hexdigest()     #Returns the encoded data in hexadecimal format
#         if(randomBirthdayHash[:R] in dictH):
#             print(hashlib.md5(dictH[randomBirthdayHash[:R]]).hexdigest(), dictH[randomBirthdayHash[:R]])
#             print(randomBirthdayHash, randomBirthday)
#             return True
#         else:
#             dictH[randomBirthdayHash[:R]] = randomBirthday
#             return False
#
# collision = False
# while(collision == False):
#     collision = randomhash()
#
# print(dictH)