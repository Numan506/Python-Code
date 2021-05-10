
print("Program 1 : "+"2+4+6+....+n "+ "(Sum of even numbers from 1-n)")

n = int(input("Enter the last number: "))
sum = 0
for x in range(2,n+1,2):
    sum = sum+x
print("Total sum is: ",sum)
print()



print("Program 2 : "+"1+3+5+....+n "+ "(Sum of odd numbers from 1-n)")

n = int(input("Enter the last number: "))
sum = 0
for x in range(1,n+1,2):
    sum = sum+x
print("Total sum is: ",sum)
print()


print("Program 3 : " + " 1*3*5*....*n "+ "(Sum of multiplications numbers from 1-n)")

n = int(input("Enter the last number: "))
sum = 1
for x in range(1,n+1,2):
    sum = sum*x
print("Total sum is: ",sum)

