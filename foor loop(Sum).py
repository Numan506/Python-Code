
num = input(" please enter the number: ")

list = num.split()
print("Total iput number is  : ", len(list))
print("number is: ")
sum = 0
for x in list:
    print(x)

    sum = sum + int(x)

print("Total num sum is = ",sum)
