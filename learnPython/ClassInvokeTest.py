class ClassInvokeTest:
    def __init__(self,name):
        self.name = name

    def sit(self):
        print(self.name);




ins  = ClassInvokeTest("TEST");
ins.sit();