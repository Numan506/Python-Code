
marks = int(input("please given the marks: "))

if marks<0 or marks>100:
    print("input is rong,please agin try ")
elif 80<=marks<=100:
    print("Result is A+")
elif 70<=marks<=79:
    print("Result is A")
elif 60<=marks<=69:
    print("Result is A-")
elif 50<=marks<=59:
    print("Result is B+")
elif 40<=marks<=49:
    print("Result is B")
elif 33<=marks<=39:
    print("Result is C")
else:
    print("Result is fail")
