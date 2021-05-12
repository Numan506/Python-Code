
from random import randint
for x in range(1,6):
       guessNumber = int(input("please enteryour number between 1 to 5 : "))
       randomNumber = randint(1, 5)
       if  guessNumber>6 or guessNumber<1:

          print("input is rong.Please try again ")
          print()

          #randomNumber = randint(1,5)

       elif guessNumber == randomNumber:
           print("you have win ")
           print()
       else:
           print("you have loss ")
           print("Random Number is",randomNumber)
           print()


print(".............Program is end")