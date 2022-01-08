#hash implementation
class Hash():
  def __init__(self,size):
    self.size=size
    self.data=[None]*self.size

  def __str__(self):
    return str(self.__dict__)

  def _hash(self,key):
    hash=0
    for i in range(len(key)):
      hash=(hash+ord(key[i])*i)%self.size
    return hash
  
  def set(self,key,value): #this method have some flwws if key is same value will be reutuned ##for first key
     hash=self._hash(key)
    if not self.data[hash]:
      self.data[hash]=[[key,value]]
    else:
      self.data[hash].append([key,value])
    print(self.data)
  
  def get(self,key):
    hash=self._hash(key)
    if self.data[hash]:
      for i in range(len(self.data[hash])):
        if self.data[hash][i][0]==key:

          return self.data[hash][i]
    
    

'''def keys 
  def values'''

a=Hash(10)
a.set("9",11)
a.set("9",10)
print(a.get("13"),"jjjjj")
print(a)
print(type(Hash))
