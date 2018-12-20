import sys;
sys.path.append('D:/pycharmWorkapce2/student');
from StudentExtend import StudentExtend

a = StudentExtend("dsffdsdf",12);
a.print_age();

# 测试property
a.namet = "testwencong";
print(a.namet)