def is_odd(n):
    return n % 2 == 1

r = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(r)

# lambda表达式
add = lambda x,y : x + y;
print(add(1,6));


# 求出一千以内的素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# print(_not_divisible(3))

print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))

# t = yield 5;
# print(t);
# print(_odd_iter())
generator = _odd_iter();
for i in generator:
    if i > 2000:
        break;
    print(i);