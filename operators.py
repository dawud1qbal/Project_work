speed = float(input("Enter speed"))

if speed > 70:
    points = 9
elif speed > 50:
    points = 6
elif speed >= 31:
    points = 3
else:
    points = 0

if points >0:
    print(F"speeding! You get {points} points.")

else:
    print("You arew within the limit.")