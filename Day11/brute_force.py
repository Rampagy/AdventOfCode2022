import math

divisors = [17, 3, 19, 7, 2, 5, 11, 13]

lcm = 1
for x in divisors:
    lcm = (lcm * x) // math.gcd(lcm, x)

print(lcm)