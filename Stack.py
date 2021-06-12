print("..........Stack...........")

# Stack works Mainly LIFO
Books = []

Books.append("C")
Books.append("Java")
Books.append("JavaScript")
Books.append("NodeJs")
Books.append("Express")
Books.append("React")
Books.append("Python")
Books.append("Django")

print("Total Subject is ", len(Books))

Books.pop()
print("Now the top Books is: ", Books[-1])

Books.pop()
print("Now the top Books is: ", Books[-1])

Books.pop()
print("Now the top Books is: ", Books[-1])

Books.pop()
print("Now the top Books is: ", Books[-1])

Books.pop()
print("Now the top Books is: ", Books[-1])

Books.pop()
print("Now the top Books is: ", Books[-1])

Books.pop()
print("Now the top Books is: ", Books[-1])

Books.pop()
if not Books:
    print("No Books Here ")

