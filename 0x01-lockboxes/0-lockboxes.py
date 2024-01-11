#!/usr/bin/python3
"""
Determines if all the boxes can be opened
Returns True or False
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    """
    if type(boxes) is not list or not boxes:
        return False

    boxLen = len(boxes)
    unlocked = [0]
    for box in unlocked:
        for key in boxes[box]:
            if key not in unlocked and key < boxLen:
                unlocked.append(key)
    if len(unlocked) == boxLen:
        return True

    return False
