#!/usr/bin/python3
""" Function that defines lockboxes"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.
    Args:
        boxes (list of list of int): A list where each index represents a box
        and each value is a list of keys contained in that box.
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n  # List to keep track of unlocked boxes
    unlocked[0] = True      # Box 0 is initially unlocked
    queue = [0]             # Start with the key to box 0

    while queue:
        current_box = queue.pop(0)  # Get the next box to process

        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)   # Add new key to the queue to explore

    return all(unlocked)
