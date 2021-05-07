
num1 = int(input("Please given the num1: "))
num2 = int(input("Please given the num2: "))
num3 = int(input("Please given the num3: "))


if (num1 >num2 and num1 > num3):
    print("large number is: ",num1)
elif(num2 >num1 and num2 >num3):
    print("large number is: ",num2)
else:
    print("large number is: ",num3)

print()


print("now print vowel or not ")

letter = input("please input any charecter: ")
letter = letter.lower()
if(letter =="a" or letter == "e" or letter =="i" or letter == "o" or letter == "u"):
    print("'" + letter + " ' " + "is vowel")
else:
    print("'" +letter +" ' " +"is consonent")


