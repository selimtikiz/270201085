def selectionSort(array):
  n = len(array)
  for i in range(n):
    
    minimum = i

    for j in range(i+1, n):
      if (array[j] < array[minimum]):
        
        minimum = j

         
    temp = array[i]
    array[i] = array[minimum]
    array[minimum] = temp
    
  return array


sort_list = [55,25,78,2,17,98,13,5]
print(selectionSort(sort_list))