
number = input("please given the number: ")
sum = 0
list = number.split() # convert list

for x in list:
    print(x)
    sum =sum + int(x)

print("Total sum is: ",sum)