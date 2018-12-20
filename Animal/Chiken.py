import sys;
sys.path.append('D:/pycharmWorkapce2/Animal');

from Animal import Animal;
from Bird import Bird;

# 继承的多个类中那个类在前面就优先使用那个类中的方法
class Chiken(Bird,Animal):

    def __init__(self,name):
        self.name = name;

    # def run(self):
    #     print("chiken is running");



# a = Chiken("test");
# a.run();