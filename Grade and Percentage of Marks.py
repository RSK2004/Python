M1 = float(input("Enter mark1:"))
M2 = float(input("Enter mark2:"))
if (M1>90):
    print("A")
elif (M1>80):
    print("B")
elif (M1>70):
    print("C")
elif (M1>60):
    print("D")
elif (M1>50):
    print("E")
else:
    print("F")
if (M2>90):
    print("A")
elif (M2>80):
    print("B")
elif (M2>70):
    print("C")
elif (M2>60):
    print("D")
elif (M2>50):
    print("E")
else:
    print("F")
sum = M1+M2
PercentageM1 = (M1/sum)*100
PercentageM2 = (M2/sum)*100
print("Percentage of M1=",PercentageM1,"%")
print("Percentage of M2=",PercentageM2,"%")
