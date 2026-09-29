p1="very nice"
p2="good keep it up"
p3="be brave"
p4="universe will help you"

message=input("enter comment")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this comment is spam")
else:
    print("not spam")