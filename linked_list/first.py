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

'''linked_list={
  head:{
    value:5,
    next:{
      value:16,
      nest:null
    }
  }
}'''
class Node:                                       #Node =[data][next]
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next


class Linkedlist:           #create a head        head= [None]->
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

  def insertValue(self,lstValue):
    self.head=None
    for i in lstValue:
      self.insertend(i)
  
  def getLen(self):
    itr=self.head
    count=0
    while itr:
      count=count+1
      itr=itr.next
    return count
  def removeat(self,pos):
    len=self.getLen()
    if pos>len:
      return ("out of index ")
    if pos==0:
      self.head=self.head.next
      return
    else:
      itr=self.head
      
      count=0
      while count<pos-1:
        itr=itr.next
        count=count+1
      
      itr.next=itr.next.next

  def insertat(self,pos,value):
    if pos==0:
      new=Node(value,self.head)
      self.head=new
      return
    if pos>self.getLen() or pos<0:
      raise Exception ("invalid index")
    else:
      count=0
      
      itr=self.head
      while count<pos-1:
        count=count+1
        itr=itr.next
      temp=itr.next
      itr.next=Node(value,temp)
      return
    print(itr.data)

      

      
      

      
      

    
      

    

     



my=Linkedlist()     
my.insertend(12)
my.insertBeg(21)
my.insertBeg(43)
my.insertend(24)
my.insertend(90)
my.insertBeg(89)
my.insertValue([1,2,3,4,5,6,7])
my.removeat(5)
my.removeat(2)
my.insertat(2,43)
my.insertat(6,46)
my.insertat(7,"hohoho")
my.insertat(0,"wth")
my.insertend("end")
my.insertBeg("Beg")
print(my)
print(my.getLen())

#Beg --> wth --> 1 --> 2 --> 43 --> 4 --> 5 --> 7 --> 46 --> hohoho --> end
#11


  



