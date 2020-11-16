a=int(input("enter a number"))
b=int(input("enter a number"))
matching_digits=0
while a>0 and b>0:
  if a%10==b%10:
    matching_digits += 1
  a=a//10
  b=b//10
print(matching_digits)