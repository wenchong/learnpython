names = ["test1","test2","test3"];
for s in names:{
    print(s)
}

for s in names:
    print(s);


sum = 99;
n = 0;
while sum > 0:
    sum = sum - 5;
    n = n + 5;
    # print(str(n) + "  wenchong")

print(eval("44"))
print(repr("44"))
print(str("44"))

a = 3.22
print(a)
print(int(a))

c = "66"
print(int(c))

a = b = c = 22;
print(b)

weg = "s";
print(str(weg))

ad = float(23);
print(ad)

def fun1(a):{
    print(a)
}
fun1("dasfdasf")
fun1(44)
fun1(123.123456)

print(range(5))
print(list(range(5)))

dicttest = {"test":"12","test2":"34","test3":"56"};
print(dicttest)
print(dicttest["test"])

print(max(1,2,3,45689))
list = [2,5,8,456,7854]
print(max(list));

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(abs(5));
# print(abs("dd"));

import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

print(move(1,2,3));
print(move(1,2,3,9));

# def quadratic(a, b, c):
#     a * math.sqrt(x) + bx + c = 0
#     return x;

# print(quadratic(1,2,3));

print(9**2);
print(math.sqrt(4));


def quadratic(a,b,c):
    key=b**2-4*a*c
    if key>0:
        x1=(-b+math.sqrt(key))/2*a
        x2=(-b-math.sqrt(key))/2*a
    if key==0:
        x1=-b/2*a
        x2=x1
    if key<0:
        print('方程无解')
        return(None,None)
    return (x1,x2)
print(quadratic(1,3,-4))

def power(x):
    return x * x

print(power(2))

# L相当于是变量
def add_end(L=[]):
    L.append('END')
    return L

print(add_end());
print(add_end());
print(add_end());

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end2());
print(add_end2());
print(add_end2());

# 关于切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[:-3])
print(L[-3:])
print(L[-3:4])

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


