import sys;
sys.path.append('D:/pycharmWorkapce2/student');
from Student import Student

class StudentExtend(Student):
    def __init__(self,name,age):
        self.name = name;
        self.score = age;

    @property
    def namet(self):
        # print(self.name + "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return self.name;

    @namet.setter
    def namet(self,name):
        self.name = name;




# a = StudentExtend("dsffdsdf",12);
# a.print_age();