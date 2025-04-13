import random, math

def random_noise():
    random_characters = ['$', '!', 'p', '-_-', ':D', '~', '@', '#']
    random_index = [random_characters[random.randint(0, len(random_characters) - 1)] for i in range(4)]

    temp = ""
    for i in random_index:
        temp = temp + i

    return temp


def hypotenuse(x, y):# the variable in the parameter and the variable being used were different 
    return math.sqrt(x**2 + y**2)

def dontprint():# print statement inside a function wont get executed without calling it 
    print("TRY TO STOP THIS FROM BEING PRINTED IN FILE a.py WITHOUT DELETING THIS PRINT STATEMENT")