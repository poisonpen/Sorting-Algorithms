# the bubble sort algorithm

def bubble_sort(array):
    for i in range(len(array)) :
        for j in range (i+1, len(array)) :
            if array[j] < array[i] :
                array[j], array[i] = array[i], array[j]
    return array

def main() :
    array = [1,323,54,23,56,78,3,34,54,20]
    sortedarray = bubble_sort(array)
    print(sortedarray)
    
main()