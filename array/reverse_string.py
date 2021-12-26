string="stranger things is awesome"
print(len(string))
def reverseString(str):
  arr=list(str)
  for i in range(len(arr)//2):
    arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
    

  
  return "".join(arr)
  
  

out=reverseString(string)
print(out)
print(len(out))


def reverseStrRecus(str):
  if str=="":
    return str
  else:
     return str[-1]+reverseStrRecus(str[:-1])
out=reverseStrRecus(string)
print(out)
