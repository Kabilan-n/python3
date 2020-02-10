weight = (input("weight: "))
unit = input("(L)bs or (K)kg: ")
if unit.upper() =="L":
    conv=weight*0.45
    print(f"your weight is {conv}")
else:
    conv=weight/0.45
    print(f"your weight is {conv}")
