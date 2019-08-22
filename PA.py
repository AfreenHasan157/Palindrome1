a=int(input())
b=a
l=0
while(a>0):
    s=a%10
    l=l*10+s
    a=a//10
if(b==l):
    print("Palindrome")
else:
    print("Not Palindrome")
