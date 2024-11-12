import time
import random

                    # Phase 1: Data Generation and Initial Sorting (Insertion Sort)

# Generating a list with random data:

def random_data(size):
    list1 = []
    # Filling the empty list with random numbers
    for x in range (0, size):
        list1.append(random.randint(1,100))
    # Printing the unsorted List
    print("List before sorting: ", list1)
    insertion_sort(list1)
    return list1

# Insertion Sort
def insertion_sort(list):
    for x in range (len(list)):
        y = x
        while list[y-1] > list[y] and y > 0:
            list[y-1], list[y] = list[y], list[y-1]
            y = y - 1 
    print("List after (insertion) sorting: ", list)
    return list


                            # Phase 2: Implement Binary Search on Sorted Data
                    # Finding the index of an element using binary search

def binary_search(list, start, end, target):
    if start > end:
        return None
    mid = (start+end)//2
    if list[mid] == target:
        return mid
    elif list[mid] < target:
        return binary_search(list, mid + 1, end, target)
    else:
        return binary_search(list, start, mid - 1, target)
    

                                # Phase 3: Recursive Merge Sort for Large Data
# We're using the random_data function again, but this time calling the merge sort function because the list is bigger

def random_data_big(size_1):
    list_2 = []
    #Fill empty list with random numbers
    for i in range (0, size_1):
        list_2.append(random.randint(1,100))
    #Print unsorted List
    print("Unsorted large list", list_2)
    merge_sort(list_2)
    print("Large List sorted using Merge Sort", list_2)
    return list_2

def merge_sort(list):
    if len(list) > 1:
        left_side = list[:len(list)//2]
        right_side = list[len(list)//2:]
        merge_sort(left_side)
        merge_sort(right_side)
        i = 0 
        j = 0 
        k = 0 
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                list[k] = left_side[i]
                i +=1
            else:
                list[k] = right_side[j]
                j += 1
            k += 1
        
        while i < len(left_side):
            list[k] = left_side[i]
            i += 1
            k += 1
        
        while j < len(right_side):
            list[k] = right_side[j]
            j += 1
            k += 1

                                        # Phase 4: Performance Comparison
# Comparing the time needed for linear search and binary in finding the same element

def time_comparison(target1, list2):
    begin = time.perf_counter()
    linear_search(target1, list2)
    end = time.perf_counter()
    print(f"Elapsed Time of Linear Search: {end-begin} seconds")
    begin1 = time.perf_counter()
    mid = binary_search(list2, 0 , len(list2), target1)
    if mid == None:
        print("Value is not in the list")
    else:
        print(f"{target1} first found at index {mid} using Binary Search")
    end1 = time.perf_counter()
    print(f"Elapsed Time of Binary Search: {end1 - begin1} seconds")

def linear_search(target1, list):
    for i in range (len(list)):
        if list[i] == target1:
            print(f"Target {target1} found first at index {i} using Linear Search")
            break
    else:
        print("Could not find target")

# Order of Phases:
# Step B cannot be activated unless Step A has been completed
# Step D cannot be activated unless Step C has been completed

def order_of_steps():
    def Step_A_and_B():
        # Step A
        size = int(input("Enter an integer for the small list (< 100): "))
        list_1 = random_data(size)
        # Step B 
        target = int(input("Enter the value out of the list you want to find: "))
        result = binary_search(list_1, 0, len(list_1), target)
        if result == None:
            print("Value is not in the list")
        else:
            print(f"Result found on index {result} using Binary Search")
    def Step_C_and_D():
        # Step C
        size_1 = int(input("Enter an integer for the large list (> 500):  "))
        list_2 = random_data_big(size_1)
        # Step D
        target_1 = int(input("Enter the value out of the list you want to find: "))
        time_comparison(target_1, list_2)

    
    return Step_A_and_B, Step_C_and_D
def main():
    Step_A_and_B, Step_C_and_D = order_of_steps()
    Step_A_and_B()
    Step_C_and_D()
    

if __name__ == "__main__":
    main()

