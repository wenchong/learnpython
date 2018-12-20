#写法一 需要手动关闭io流
try:
    f = open('test1.txt', 'r');
    a = f.read();
    print(a)
finally:
    if f:
        f.close()

#写法二 读完以后手动关闭io流
with open('test1.txt', 'r') as f:
    a = f.read();
    print(a)

#关于读
# with open("test1.txt",'w') as f:
#     f.write("hello python");

with open("test1.txt",'a') as f:
    f.write("hello python");
