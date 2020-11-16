password= "abc123"

giris=str(input("enter the password"))
if(password==giris):
  print("login is successful")
else:
  while(password!=giris):
    giris=str(input("enter the password again"))
    if(giris=="help"):
      print("a")
    else:
      print("wrong password")
print("login successfully")

