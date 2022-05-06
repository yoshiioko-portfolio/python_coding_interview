"""
    Problem Statement
    Implement a function that removes all the even elements from a given list. Name it remove_even(lst).

    Input
    A list with random integers.

    Output
    A list with only odd integers

    Sample Input
    my_list = [1,2,4,5,10,6,3]
    Sample Output
    my_list = [1,5,3]
"""


# Time: O(n)
# Space: O(n)
def remove_even(lst):
    # Write your code here!
    odd_list = []

    for number in lst:
        if number % 2 != 0:
            odd_list.append(number)

    return odd_list


def remove_even_pythonic(lst):
    return [number for number in lst if number % 2 != 0]


expected_result = [1, 5, 3]

my_list = [1, 2, 4, 5, 10, 6, 3]
print(expected_result == remove_even(my_list))

print(expected_result == remove_even_pythonic(my_list))
