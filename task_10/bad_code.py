''' some dice thing '''
from random import randint

DICE_ROLL_NUMBER = 6
def rolllotsofdice():
    ''' random number from 1 to 6 '''
    return randint(1,6)
print(rolllotsofdice())

def rolllotsofdice2():
    ''' random number from 1 to 10 '''
    return randint(1,10)

def rollcustonnumbersss(numberone, numbertwo,):
    ''' generates random number '''
    return randint(numberone, numbertwo)

def checkrolls():
    ''' returns if the number if over 6 '''
    if rolllotsofdice2() >= 6:
        return "big number!!!"
    return "small number :( "

CHECK_ROLLS_VAR= checkrolls()

print(CHECK_ROLLS_VAR)
LONG_VAR_NAME = """this is a really long variable that is integral to the flow of the code,
if this variable is to become any shorter the code will simply fail as this is a fundamental piece of code for the really important and really resilient code base..
 how many chars now??"""
