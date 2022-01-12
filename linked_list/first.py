##arrys has very bad performanc
##no use arrays
#use hash tables or
#use linked list linked list
#linked list are collision in hash tables
#singly linked list and doubly linked list
# linked list are no termination
# linked list are slow in iteration
#garbage collected language delete memory automaicllay and non garbage is totally we use memory
basket=['apples','grapes','pears']
#linked list apples->grapes->pears->null
obj1={"a":"true"}
obj2=obj1
obj1="dray"
print(obj1,obj2)
'''linked_list={
  head:{
    value:5,
    next:{
      value:16,
      nest:null
    }
  }
}'''
class Node():                                       #Node =[data][next]
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next


class Linkedlist():           #create a head        head= [None]->
  def __init__(self):
    self.head=None
   
  def insertBeg(self,value):      # node=[value][None]
    node=Node(value,self.head)           # head= [value][None]
    self.head=node
  
  def __str__(self):
    if self.head is None:
      return ("linked list is empty")
    itr=self.head
    itrls=""
    while itr:
      itrls += str(itr.data)+' --> ' if itr.next else str(itr.data)
      itr = itr.next
    return (itrls)
  
  

  def insertend(self,value):
    if self.head is None:
      self.head=Node(value,self.head)
    
    else:
      temphead=self.head
      while temphead.next!=None:
        temphead=temphead.next
      temphead.next=Node(value,None)

  def createNew(self,arr):
    
      

    

     



my=Linkedlist()     
my.insertend(12)
my.insertBeg(21)
my.insertBeg(43)
my.insertend(24)
my.insertend(90)
my.insertBeg(89)
print(my)

  



