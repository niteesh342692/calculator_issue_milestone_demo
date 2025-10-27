def add(a, b): return a + b
def sub(a, b): return a - b
def multi(a, b): return a * b
def divi(a, b):
  if(b == 0): return 'Divisor is Zero, unable to divide'
  return a / b
def mod(a, b):
  if(b == 0): return 'Divisor is Zero, unable to divide'
  return a % b

a, b = int(input()), int(input())
print(add(a, b))
print(sub(a, b))
print(multi(a, b))
print(divi(a, b))
print(mod(a, b))


def mile_to_km(miles): return miles * 1.62
