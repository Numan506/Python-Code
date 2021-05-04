
num1 = int(input("please given the num1: "))
num2 = int(input("please given the num2: "))
num3 = int(input("please given the num3: "))
print()

if (num1>num2 and num1>num3):
    print("big number is: ",num1)
elif(num2>num1 and num2>num3 ):
    print("big number is: ",num2)
else:
    print("big number is: ",num3)
print()


print(".........Now we show that vowel or consonent..........")

letter = input("enter the charecter: ");
letter=letter.lower()

if (letter=="a" or letter =="e" or letter=="i" or letter=="o" or letter =="u"):
    print("This is a vowel")
else:
    print("This is a consonenet")
