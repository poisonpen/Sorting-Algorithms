# the selections sort algorithm
array = [1,323,54,23,56,78,3,34,54,20];

for i in range(len(array)):
    min_idx = i
    for j in range (i+1, len(array)):
        if array[j] < array[min_idx] :
            min_idx = j
    #put min_idx element in ith position
    array[min_idx], array[i] = array[i], array[min_idx]
    
print(array)