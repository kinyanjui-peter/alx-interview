#!/usr/bin/python3
"""This is an interview question, lockboxes,can all boxes be opened"""


def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
