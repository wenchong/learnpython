class Bird(object):
    def _init_(self,name):
        self.name = name;

    @property
    def nameg(self):
        return  self.name;

    def run(self):
        print("bird is fly");