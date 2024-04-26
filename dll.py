class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new

    def print(self):
        if self.head==None:
            return
        i=self.head
        while i:
          print(i.data)
          i=i.next
l=[1,2,3,4,5]
o=dll()
for i in range(1,6):
    o.insertatbeg(i)
o.print()
