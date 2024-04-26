class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
   # def insertatbeg(self,data):
   #     if self.head==None:
   #         self.head=node(data)
   #     else:
   #         new=node(data)
   #         new.next=self.head
   #         self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new =node(data)
            i=self.head
            while i.next:
                i=i.next
            i.next=new
    def printing(self):
        if self.head==None:
            return
        i=self.head
        while i:
            print(i.data)
            i=i.next
    def length(self):
        count=0
        i=self.head
        while i:
            count+=1
            i=i.next
        return count
l=[1,2,3,4,5]
o=sll()
for i in l:
   # o.insertatbeg(i) 
   o.insertatend(i)
o.printing()
print(o.length())
#print(head.data,head.next.data)
#a=node(1)
#a.next=node(2)
#a.next.next=node(3)
#print(a,a.data,a.next)
#print(a.next,a.next.data,a.next.next)
#print(a.next.next,a.next.next.data,a.next.next.next)