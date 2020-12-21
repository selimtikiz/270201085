ls = [0,1,2,3,4,5]

def get_number_of_evens():
    v=0
    for i in range(0,len(ls)):
        if ls[i]%2 == 0:
            v+=1
    print(v)

get_number_of_evens()