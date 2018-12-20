class Animal(object):
    def _init_(self,name):
        self.name = "Animal";

    @property
    def nameg(self):
        return self.name;

    def run(self):
        print("animal can fly and run");