import math
 
def gcd(a, b):
    return math.gcd(a, b)
 
def solve():
    y, w = map(int, input().split())
    target = max(y, w)
    winning_outcomes = 6 - target + 1
    
    if winning_outcomes == 0:
        print("0/1")
        return
 
    if winning_outcomes == 6:
        print("1/1")
        return
 
    common_divisor = gcd(winning_outcomes, 6)
    numerator = winning_outcomes // common_divisor
    denominator = 6 // common_divisor
    print(f"{numerator}/{denominator}")
 
solve()
