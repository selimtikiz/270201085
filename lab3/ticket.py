age = int(input("what is your age"))
ucret = 3
if(age<=6) and (age>=60):
  print("ücretsiz")
elif(age>18) and (age<60):
  print(ucret ,"TL")
else:
  print(float(ucret/2),"TL")
