eq1 = input("enter the first equation")
eq1lst = list(eq1)
print(eq1lst)
eq1lst1 = eq1.split("=")
eq1lst1str1 ="".join(eq1lst1[0])
eq1lst1str2 ="".join(eq1lst1[1])
print(eq1lst1)
sumof_x1 = 0
sumof_x2 = 0
sumof_y1 = 0
sumof_y2 = 0
for i in range(0,len(eq1lst1str1[0])):
    if(eq1lst1str1[i] == "x"):
        x1 = int(eq1lst1str1[i-2:i])

        print("x1:",x1)
        sumof_x1 += x1
        print(sumof_x1)

#BURADAN DEVAM ET ( 2. FOR DONGUSUNE NASIL GIRILECEGINI BUL) LIST TO STRING YAPTIK EN SON

for j in range(0,len(eq1lst1str1[0])):
    if(eq1lst1str1[j] == "y"):
        y1 = eq1lst1str1[j-2:j]
        print("y1:",y1)
        sumof_y1 += y1
        print(sumof_y1)


for k in range(0,len(eq1lst1str2[1])):
    if(eq1lst1str2[k]== "x"):
        x2 = eq1lst1str2[k-2:k]
        print("x2:",x2)

for h in range(0,len(eq1lst1str2[1])):
    if (eq1lst1[h] == "y"):
        y2 = eq1lst1str2[h-2:h]
        print("y2:",y2)

