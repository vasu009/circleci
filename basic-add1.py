class AB:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

obj = AB(3,4)

print(obj.addition())