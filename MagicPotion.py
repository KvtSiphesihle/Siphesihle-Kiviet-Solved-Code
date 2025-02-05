import math

def is_magical_potion(power):
    cube_root = round(power ** (1/3))
    if cube_root ** 3 == power:
        return "YES"
    else:
        return "NO"

power = 132651201231
print(is_magical_potion(power))


"""  In order To determine if a given power level is a magical potion, we need to check if the power level is a perfect cube. A perfect cube is an integer that can be expressed as n to the power 3, where 
n is an integer
I also used a online cube root calculators to manually check if the cube root is an integer.
I wrote a simple Python script to check if a number is a perfect cube. """