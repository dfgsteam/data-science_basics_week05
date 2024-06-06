def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


"""
Sorts a list in ascending order using the merge sort algorithm.

Parameters:
- list_to_sort_by_merge (list): The list to be sorted.

Returns:
- None. The list is sorted in-place.

"""
def mergeSort(list_to_sort_by_merge):
    if len(list_to_sort_by_merge) > 1:
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                # Assign the value from the left list to the merged list
                list_to_sort_by_merge[i] = left[l]
                l += 1
            else:
                # Assign the value from the right list to the merged list
                list_to_sort_by_merge[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            # Assign the remaining values from the left list to the merged list
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            # Assign the remaining values from the right list to the merged list
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
