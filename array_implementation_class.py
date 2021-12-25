class My():
  def __init__(self):
    self.length=0
    self.data={}
  
  def __str__(self):
       return str(self.__dict__)

  def get(self,index):
    if index>self.length-1:
      print("index outof range for get statement")
    else:
       return self.data[index]

  def push(self,val):
    self.length=self.length+1
    self.data[self.length-1]=val
  
  def pop(self):
    if self.length<1:
      print("pop not possible ,no item available")
    else:
     last=self.data[self.length-1]
     del self.data[self.length-1]
     self.length=self.length-1
     return last
  
  def delete(self,index):
    if index>self.length-1:
      print("delete item not possible index out of range")
    else:
      for i in range(index,self.length-1):
        self.data[i]=self.data[i+1]
      del self.data[self.length-1]
      print("item deleted at index",index)
      self.length=self.length-1

  def insert(self,index,val):
     if index>self.length:
       for i in range(self.length,index):
         self.data[i]=None               #very important point it can help you to insert value at any index
       self.data[index]=val
     else:
       for i in range(self.length,index,-1):
         self.data[i]=self.data[i-1]
       self.data[index]=val



new=My()
new.push(23)
new.push(55)
new.push(34)
new.push(35)
new.push(36)
new.push(37)
print(new)
new.insert(9,88)
print(new)
new.insert(2,90)

print(new)


''' out will be
{'length': 6, 'data': {0: 23, 1: 55, 2: 34, 3: 35, 4: 36, 5: 37}}
{'length': 6, 'data': {0: 23, 1: 55, 2: 34, 3: 35, 4: 36, 5: 37, 6: None, 7: None, 8: None, 9: 88}}
{'length': 6, 'data': {0: 23, 1: 55, 2: 90, 3: 34, 4: 35, 5: 36, 6: 37, 7: None, 8: None, 9: 88}}
'''
