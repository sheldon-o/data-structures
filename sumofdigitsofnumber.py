#input =545
#output=5+4+5=14=1+4=5
#output=5


print("Hello world")
N=int(input())


def iamurpapa(num):
    if num<10:
        print(num)
        return (num)
    
    else:
        output=0
        while(num>0):
            rem=num%10
            output+=rem
            num=num//10
    iamurpapa(output)
y=iamurpapa(N)
print(y,"hwhw")
