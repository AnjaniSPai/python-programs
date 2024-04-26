class a:
    branch="cse"
    def fun1 (self):
        print("fun1")
    def fun2 (self): 
        a.x=10
        self.a=a
        print("fun2",self.branch)
class b(a):
    def __init__(self)->None:
        print("1")            
    def __init__(self)->None:
        print("2")
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun4")
class c(b):
    def __init__(self)->None:
        print("1")            
    def __init__(self)->None:
        print("2")
    def fun5(self):
        print("fun5")
    def fun6(self):
        print("fun6")        
o=a()
p=b()
q=c()
p.fun3()
q.fun5()
o.fun2()
            