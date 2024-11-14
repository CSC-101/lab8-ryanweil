# group.py

from typing import List


def groups_of_3(numbers: List[int]) -> List[List[int]]:
    """
    Groups the elements of the input list into groups of three values.

    Parameters:
        numbers (List[int]): A list of integers to group.

    Returns:
        List[List[int]]: A list of lists, where each sublist contains up to three integers.
    """
    grouped_list = []
    for i in range(0, len(numbers), 3):
        grouped_list.append(numbers[i:i + 3])
    return grouped_list
