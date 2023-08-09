# 快排
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# 前缀树
def prefix_tree(arr):
    tree = {}
    for i in arr:
        t = tree
        for j in i:
            if j not in t:
                t[j] = {}
            t = t[j]
    return tree


# 最大堆
def max_heap(arr):
    for i in range(len(arr)):
        j = i
        while j > 0:
            p = (j - 1) // 2
            if arr[j] > arr[p]:
                arr[j], arr[p] = arr[p], arr[j]
                j = p
            else:
                break
    return arr
