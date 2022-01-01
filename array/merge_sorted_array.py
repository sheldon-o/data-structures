'''given two array which are sorted ,you have to merge them so that new array is also sorted'''

arr1=[1,2,4,15,32,69,101]
arr2=[2,6,10,14,16,67,98,100]
def mergeSortedArray(arr1,arr2):
  

  
  out=[]
  i=0
  j=0
  k=0
  while(j<len(arr2) and i<len(arr1)):
    
    if arr1[i]>arr2[j]:
      out.append(arr2[j])
      
      j=j+1
      k=k+1
      
      
      
     
    else:
      out.append(arr1[i])
      
      i=i+1
      k=k+1
  while (i<len(arr1)):
    out.append(arr1[i])
    i=i+1
  while (j<len(arr2)):
    out.append(arr2[j])
    j=j+1

  return(out)
      
out=mergeSortedArray(arr1,arr2)
print(out)
