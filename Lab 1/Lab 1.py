#2+3=5
#2*3=6
#2**3=8
#49//3=16
#49/3=16.33332
#49/3.0=16.33332
#49%3=1
#4*3+17//2-5=15
#4*(3+17)//2-5=35
#4*3+(17//2)-5=15
#4*(3+17)//(2-5)=-27

a=1+2
print(a)

x = 3**2 # What is the value of x? =9
y = 4**2 # What is the value of y? What does the ** operator do? y=16 It raised it to the power of 2
z = x * y # What is the value of z? z=144
print()

a = 2
b = a + 1 # What is the value of b? 3
a = 9 # What is the value of a? What is the value of b? a=9 b=10
print()

a = not True # What is the value of a? a=False
x = a and True or False # What is the value of x? x=False
print()

def function1(x, y):
    z = x + y * 2
    return z + 4
result = function1(2*2, 4 - 1)

# When asked, step into the call that must be evaluated first.
def square(n:float) -> float:
    return n * n # What is the value first returned by square? What was n? first n:2. the value of n was 2

result = square(square(2)) # What is the value of result? 16
print()

def function2(a:int, b:int) -> int:
    c = a + b # Are a and b here related to a and b before the call? no a:7 and b:9
    return c**2 # What is the value returned by the function? 256

a = 9
b = 7
answer = function2(b, a) # What is the value of answer? 256
print() # What happened to c? c is erased or no longer works