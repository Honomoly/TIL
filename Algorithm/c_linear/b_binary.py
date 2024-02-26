# 이진탐색

# 오름차순 조건
def bin_search(arr, key):
    pl = 0
    pr = len(arr) - 1
    while pl <= pr:
        center = (pl + pr) // 2
        if arr[center] == key:
            return center
        elif key > arr[center]:
            pl = center + 1
        else:
            pr = center - 1
    return -1

print(bin_search([1, 4, 53, 143, 787, 1001], 53))