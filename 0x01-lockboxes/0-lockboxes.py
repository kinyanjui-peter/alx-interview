#!/usr/bin/python3
"""This is an interview question, lockboxes,can all boxes be opened"""


def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return False

    keys = set([0])
    # Start with the keys to the first box (index 0)
    unlocked = set()
    while keys:
        box_idx = keys.pop()
        # Get the index of the box with the key
        unlocked.add(box_idx)
        # Mark the box as unlocked
        # Add all new keys found in the opened box
        keys.update(boxes[box_idx])
        # Remove keys to already opened boxes
        keys.difference_update(unlocked)
    return len(unlocked) == len(boxes)
