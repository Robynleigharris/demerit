#80-100 A
#70-79 B
#69-50 C
#40-49 D
#0-39 E

"""mark=int(input("please enter mark of student"))
if mark>=80 and mark<=100:
 print("grade A")
elif mark>=70 and mark<=79:
 print("grade b")
elif mark>=50 and mark<=69:
 print("grade c")
elif mark>=40 and mark<=49:
 print("grade D")
else:
 print("grade E")
if not isinstance(mark, int):
 print("Wrong input")"""


speed=int(input("what was your average speed"))
allowed=int(input("what was your allowed speed"))

if(speed ==allowed):
    print("OK")

elif (speed>=60):
    current_speed=(speed-allowed)
    print(current_speed)

    demerit=current_speed//5
    print(demerit)

    if demerit>=12:
        print("time to go to jail")



