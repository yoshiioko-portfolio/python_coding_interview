"""
    Problem Statement
    Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).

    Input
    Two sorted lists.

    Output
    A merged and sorted list consisting of all elements of both input lists.

    Sample Input
    list1 = [1,3,4,5]
    list2 = [2,6,7,8]
    Sample Output
    arr = [1,2,3,4,5,6,7,8]
"""


# Time: O(m + n), where m and n are the lengths of the lists
# Space: O(m + n)
def merge_lists(lst1, lst2):
    # Write your code here
    merged = []

    index_1 = 0
    index_2 = 0
    while index_1 < len(lst1) and index_2 < len(lst2):
        if lst1[index_1] < lst2[index_2]:
            merged.append(lst1[index_1])
            index_1 += 1
        else:
            merged.append(lst2[index_2])
            index_2 += 1

    while index_1 < len(lst1):
        merged.append(lst1[index_1])
        index_1 += 1

    while index_2 < len(lst2):
        merged.append(lst2[index_2])
        index_2 += 1

    return merged


list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]
arr = [1, 2, 3, 4, 5, 6, 7, 8]

print(arr == merge_lists(list1, list2))
