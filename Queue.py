
from collections import  deque

# queue works mainly FIFO
person = deque(["Numan","Rakib","Khalek","Faysal"])
print("Total person is ", len(person))

person.popleft()
print("Now left person is: ",person[0])

person.popleft()
print("Now left person is: ",person[0])

person.popleft()
print("Now left person is: ",person[0])

person.popleft()
if not person:
    print("No person left")
