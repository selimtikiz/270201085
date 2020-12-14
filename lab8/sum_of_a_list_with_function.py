def my_function(a):
    summ = 0
    for i in range(0,a):
        summ += i
    summ = summ*summ
    return summ

n = int(input("enter range of sequence"))
print(my_function(n))