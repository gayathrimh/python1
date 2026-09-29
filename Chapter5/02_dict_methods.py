marks={
    "gayathri":56,
    "rohan":100,
    "sushan":80
}
#print(marks.items())    #will get tuples
#print(marks.keys())
#print(marks.values())
#marks.update({"gayathri":99,"renuka":100})  #updates marks
#print(marks)

#print(marks.get("soumys"))  #nothing
#print(marks.get("gayathri"))

#print(marks.get("gayathri"))    #gives 56
#print(marks["gayathri"])    #gives 56

#print(marks.get("gayathri2"))   #prints none->by using get returns none for variable gayathri2
print(marks["gayathri2"])   #returns error

