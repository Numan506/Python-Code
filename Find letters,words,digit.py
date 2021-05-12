
num_of_letters = 0
num_of_words = 1
num_of_digit = 0

text = input("please given the text: ")
for x in text:
      x = x.lower()
      if x >="a" and x <="z":
           num_of_letters = num_of_letters+1
      elif  x >="0" and x<="9":
           num_of_digit = num_of_digit+1
      elif x ==  ' ':
          num_of_words =num_of_words+1

print("Total Number of Letters = ",num_of_letters)
print("Total Number of Digits = ",num_of_digit)
print("Total Number of Words = ",num_of_words)