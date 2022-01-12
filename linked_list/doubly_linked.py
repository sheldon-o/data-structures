
print("hey")
class Node:
  def __init__(self,data=None,prev=None,next=None):
    self.data=data
    self.next=next
    self.prev=prev
  
class LinkedList:
  def __init__(self):
    self.head=None
    
  def insertBeg(self,value):
    if self.head==None:
      node=Node(value,None,self.head)

      self.head=node
      return
    else:
      node=Node(value,None,self.head)
      self.head=node
      self.head.next.prev=self.head
  def __str__(self):
    if self.head==None:
      return("you are empty my boy")
    itr=self.head
    itrls=""
    while itr:
      itrls=itrls+str(itr.data)+"-->"
      itr=itr.next
      
    return itrls
  
  def getLen(self):
    count=0
    itr=self.head
    while itr:
      count=count+1
      itr=itr.next
  
  def insertEnd(self,value):
    if getLen(self)==0:
      insertBeg()
    
    
    
  
my=LinkedList()
my.insertBeg(1)
my.insertBeg(2)
my.insertBeg(3)
my.insertBeg(5)
my.insertBeg(1)
print(my)