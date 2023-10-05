#!/usr/bin/python3
'''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
'''


def canUnlockAll(boxes):
    if type(boxes) != list or len(boxes) == 0:
        return False

    boxLength = len(boxes)

    freeKeys = [0]
    usedKeys = set()

    while freeKeys:
        openedBoxIndex = freeKeys.pop()
        usedKeys.add(openedBoxIndex)

        openedBox = boxes[openedBoxIndex]

        if type(openedBox) != list:
            return False

        for key in openedBox:
            if (key not in freeKeys) and (key not in usedKeys) and \
                    (key < boxLength):
                freeKeys.append(key)

    return len(usedKeys) == boxLength
