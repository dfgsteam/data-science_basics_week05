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
            k += 1

        while r < len(right):
            # Assign the remaining values from the right list to the merged list
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1

    return input_list

def visualize_sorting(input_list):
    """
    Visualizes the sorting process using matplotlib.

    Args:
        input_list (list): The list to be sorted and visualized.
    """
    x = np.arange(len(input_list))

    # Sort the list
    sorted_list = merge_sort(input_list.copy())

    # Plot the unsorted and sorted list in the same diagram
    plt.figure(figsize=(10, 6))
    plt.plot(x, input_list, label='Unsorted', color='blue', marker='o')
    plt.plot(x, sorted_list, label='Sorted', color='green', marker='o')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Visualization of Merge Sort')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    example_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    visualize_sorting(example_list)

