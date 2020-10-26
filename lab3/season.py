month =(int(input("enter the month")))
day =(int(input("enter the day")))

if(month>=3) and (day>=20):
  print("spring")
elif(month>=6) and(day>=21):
  print("summer")
elif(month>=9) and (day>=22):
  print("fall")
else:
  print("winter")