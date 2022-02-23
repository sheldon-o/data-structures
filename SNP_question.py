# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
'''print("Hello world")
s="aabssbccjjegg"
dic={}
for i in s:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
for j in dic:
    if dic[j]==1:
        print(j)'''
        
        
#palindrome
s="jijiikkk"
dic={}
for i in s:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
odd_count=0
even_count=0
if len(s)%2==0:
    flag=False
    for j in dic:
        if dic[j]%2!=0:
            print ("not possible pallindrome")
            flag=True
            break
    if flag==False:
        print ("possible pallindrome")
else:
    for j in dic:
        if dic[j]%2!=0:
            odd_count+=1
    if odd_count>1:
        print("not possible")
    else:
        print("possible pallindrome")
        
        
    
