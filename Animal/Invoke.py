import sys;
sys.path.append('D:/pycharmWorkapce2/Animal');

from Chiken import Chiken


a = Chiken("chiken");
a.run();

print(type(a));