import random
import time

# set a fixed seed for the random module to ensure reproducibility
random.seed(42)

# implementation of binary search

# I will prove that binary search is faster than naive search

# naive search scans the whole list and ask if its equal to the target 
# if yes return the index
# if no then return -1

def naive_search(l, target):
    # example: l = [1, 3, 10,  12] let's say we are searching for '10'
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer algorithm
# we will leverage the fact that our list is sorted
def binary_search(l, target, low=None, high=None):
    # set the default values for low and high if not given
    if low is None:
        low = 0
    if high is None:
        high = len(l) -1
        
    # check if the list is empty or the target is out of range
    if high < low:
        return -1
        
    # example: l = [1, 3, 5, 10, 12] let's say we are searching for '10' again (it should return index(3) because the index 0)
    # find the midpoint of the list by integer division
    midpoint = (low + high) // 2
    
    # compare the target with the element at the midpoint
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        # if the target is smaller than the midpoint, search in the left half of the list
        return binary_search(l, target, low, midpoint -1)
    else:
        # if the target is larger than the midpoint, search in the right half of the list
        return binary_search(l, target, midpoint + 1, high)
    
if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))
    
    length = 10000 # to increase the binary search performance
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))
    
    # measure the execution time of naive search using time.time()
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")
    
    # measure the execution time of binary search using time.time()
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")
    
    # this is to prove that binary search is much faster
