num= int(input("enter the number of number"))

evens=0
for i in range(num):
  number=float(input("enter a number"))
  if(number%2==0):
    evens += 1
print(evens/num*100,"%")