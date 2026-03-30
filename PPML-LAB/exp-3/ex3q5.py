m1=float(input("subject 1 mark:"))
m2=float(input("subject 2 mark:"))
m3=float(input("subject 3 mark:"))
m4=float(input("subject 4 mark:"))
m5=float(input("subject 5 mark:"))
percentage=((m1+m2+m3+m4+m5)/250)*100
print("percentage:",percentage)
if (percentage>=90 and percentage<=100):
    print("Grade is O")
elif (percentage>=80 and percentage<90):
    print("Grade is E")
elif (percentage>=70 and percentage<80):
    print("Grade is A")
elif (percentage>=60 and percentage<70):
    print("Grade is B")
elif (percentage>=50 and percentage<60):
    print("Grade is C")
elif (percentage>=0 and percentage<50):
    print("Grade is F")
else: 
    print("Invalid marks")
