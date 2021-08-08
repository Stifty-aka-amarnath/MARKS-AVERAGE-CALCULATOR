s1=int(input("enter first subject marks"))
s2=int(input("enter second subject marks"))
s3=int(input("enter third subject marks"))
s4=int(input("enter fourth subject marks"))
s5=int(input("enter fifth subject marks"))
total = s1+s2+s3+s4+s5
avg=round(total/3,2)
if avg >90:
    g="A1"
elif avg >80:
    g="A2"
elif avg >70:
    g="B1"
elif avg>60:
    g="B2"
elif avg>50:
    g= "C1"
elif avg>40:
    g="C2"
elif avg>=33:
    g+"D"
else:
    g="E"
print("total marks  :",total)
print("average marks:",avg)
print("grade        :",g)