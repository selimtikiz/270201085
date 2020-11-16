my_list=[12,31,17,85,39,56,22,81,16,57,23]
a="syntax"
b=len(a)**2

if b in my_list:
  print(my_list +[a])
else:
  print(my_list+[b,a])