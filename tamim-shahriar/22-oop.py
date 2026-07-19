import math

class Fraction:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d
        
    def add(self, f):
        lcm = math.lcm(self.denominator, f.denominator)
        
        num = (lcm / self.denominator ) * self.numerator + \
            (num / f.denominator) * f.numerator
            
        self.numerator = int(num)
        self.denominator = lcm
        
def __add__(self, f):
    lcm = math.lcm(self.denominator, f.denominator)
    
    num = (lcm / self.denominator) * self.numerator + \
        (lcm / f.denominator) * f.numerator
        
    return Fraction(int(num), lcm)

def __str__(self):
    return "{} / {}".format(self.numerator, self.denominator)

def __eq__(self, f):
    g = math.gcd(self.numerator, self.denominator)
    num1 = self.numerator // g
    denom1 = self.denominator // g
    
    g = math.gcd(f.numerator, f.denominator)
    num2 = f.numerator // g
    denom2 = f.denominator // g
    return num1 == num2 and denom1 == denom2

def __ne__(self, value:object) -> bool:
    pass

def __gt__(self):
    pass

def __lt__(self):
    pass

f1 = Fraction(5, 10)
f2 = Fraction(10, 20)

print(f1 > f2)
print(f1)
print(f2)

print( f1 + f2)