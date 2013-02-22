def chopIterative(target, list):
    first = 0
    last = len(list) - 1
    while first <= last:
        mid = int(round((first + last) / 2))
        if list[mid] is target:
            return mid
        if list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return - 1


def chopRecursive(target, list):
    return recursiveHelper(target, list, 0, len(list) - 1)


def recursiveHelper(target, list, first, last):
    if first > last:
        return - 1
    mid = int(first + round((last - first) / 2))
    if list[mid] < target:
        return recursiveHelper(target, list, mid + 1, last)
    elif list[mid] > target:
        return recursiveHelper(target, list, first, mid - 1)
    else:
        return mid


def chopSliceRecursive(target, list):
    return sliceRecursiveHelper(target, list, 0)


def sliceRecursiveHelper(target, list, offset):
    if not list:
        return - 1
    mid = int(round((len(list)) / 2))
    if list[mid] < target:
        return sliceRecursiveHelper(target, list[mid + 1:], mid + 1)
    elif list[mid] > target:
        return sliceRecursiveHelper(target, list[: mid], offset)
    else:
        return offset + mid


def chopSliceIterative(target, list):
    offset = 0
    while (list):
        mid = int(round((len(list)) / 2))
        if list[mid] is target:
            return offset + mid
        if list[mid] < target:
            offset = mid + 1
            list = list[mid + 1:]
        else:
            list = list[: mid]
    return - 1


def chop(target, list):
    if not list:
        return - 1
    mid = int(round((len(list)) / 2))
    print (mid, list)
    if list[mid] < target:
        ret = chop(target, list[mid + 1:])
        if ret is - 1:
            return ret
        else:
            return mid + 1 + ret
    elif list[mid] > target:
        return chop(target, list[: mid])
    else:
        return mid