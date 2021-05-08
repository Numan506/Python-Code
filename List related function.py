
language = ["python","java","javaScript","node js","c","c++"];

print("Total length is: ",len(language)); # find to length

language.append("django") # add new language
print("new language add list,and name is: ",language)

language.insert(2,"react js") # add a new language ,index number 2
print("new language add list and name: ",language)

language.remove("c++")
print("now language list is: ",language) # remove any language name

language.sort()
print("ascending is ",language) # small to big ascending language list,

language.reverse()
print("descending is ",language) # big to small language list

language.pop()
print("after pop language list is: ",language) # last language is delete

pos = language.index("python")
print("python ,language index number is ",pos) # find to position

