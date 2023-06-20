#import timeit

print("Asending")
print("")

#insert sort
def insertion_sort(array):
    start = timeit.default_timer()
    for i in range(1,len(array)):
        item = array[i]
        j = i - 1
        
        while j >= 0 and array[j] > item:
            array[j+1] = array[j]
            j -=1
            
            array[j+1] = item  
    stop = timeit.default_timer()
    print(f"insertion sort successful! Elapsed time: + {stop - start}")
    return array

#bubble sortin
def bubble_sort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        for j in range(len(array)):
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
    
    stop = timeit.default_timer()
    print(f"buble sort succesful! Elaspsed time: {stop - start}")
    return array


list_1 = [8,3,1,2,9,67,4,33,]
print(f"Before: {list_1}")
bubble_sort(list_1)
print(f"After: {list_1}")