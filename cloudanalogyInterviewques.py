#find the second largest element in array
print("Hello world")
arr=[1,2,34,3,1,3,5,97,97,98,98,3,2,4,55,65,43]
largest=arr[0]
second_largest=arr[0]
for i in range(len(arr)):
    if arr[i]>=largest:
        if arr[i]!=largest:
            second_largest=largest
            largest=arr[i]
    else:
        if arr[i]>second_largest:
            second_largest=arr[i]
print(largest,second_largest)
