import math




def volume(radius):
    v = 4/3 * math.pi * radius**3
    return v


print(volume(5))

def area(radius):
    a = 4 * math.pi * radius**2
    return a

print(area(8))


def unicost(inches, cost):
    u= inches * cost
    return u

print(unicost(9, 5))
