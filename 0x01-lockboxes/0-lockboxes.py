#!/usr/bin/python3
"""
Determines if all the boxes can be opened
Returns True or False
"""
def canUnlockAll(boxes):
    len = len(boxes)
    visited = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)
        for key in boxes[current_box]:
            if key < len and key not in visited:
                queue.append(key)

    return len(visited) == len