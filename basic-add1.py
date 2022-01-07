class AB:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        return f"After adding {self.a} and {self.b} is : {self.a + self.b}"

    
    def git(self):
        print("sucessfully integrated with CircleCi")

obj = AB(3,4)

print(obj.addition())

obj.git()