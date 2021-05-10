
print("..................Program 1................")
n = int(input("please enter the number: "))

for i in range(n+1):
    print(i*"*")
print()

print("..................Program 2................")
n = int(input("please enter the number: "))

for i in range(1,n+1,2):
    print(i*"*")
print()

print("..................Program 3................")
n = int(input("please enter the number: "))

for i in range(1, n+1) :
    print((n-i) * " ",end=" ")
    print(i * "*")
