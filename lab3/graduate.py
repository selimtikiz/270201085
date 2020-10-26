gpa = float(input("gpa giriniz"))
nol = float(input("number of lectures"))

if(gpa/nol<2) and (nol<47):
  print("not enough number of lectures and gpa")
if(gpa/nol<2) and (nol>=47):
  print("Not enough Gpa")
if(gpa/nol>=2) and (nol<47):
  print("not enough number of lectures")
if(gpa/nol>=2) and (nol>=47):
  print("Graduated")