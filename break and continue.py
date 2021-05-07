num1 = int(input("please enter the num1:  "))
num2 = int(input("please enter the num2:  "))

i = 0
while(i<=num1):
    if(i == num2):
        break
    i = i+1
    print(i)
print("break program is end ")
print()


print("........now show continue program......... ")


num1 = int(input("please enter the num1:  "))
num2 = int(input("please enter the num2:  "))
i = 0
while(i<=num1):
    i = i+1
    if (i==num2):
        continue
    print(i)
print(" Continue Program is end")