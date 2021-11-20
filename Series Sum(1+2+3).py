
num =[10,20,30,40]
value = len(num)-1
result = (num[value])
sum =0

for x in num:
    print(x,end="")
    if(x== result):
        break
    print("+",end="")
    sum=sum+x


print(" =",sum)