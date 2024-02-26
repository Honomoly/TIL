from Algorithm.tools import Queue, Stack

# Confirm Sort
def is_sorted(arr):
    flag = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            flag = False
            break
    return flag

# Bubble Sort
def bubble_sort1(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort2(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort3(arr):
    for i in range(len(arr)-1):
        flag = True
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False
        if flag:
            break
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min = arr[i]
        idx = i
        for j in range(i, len(arr)):
            if min > arr[j]:
                min = arr[j]
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr

# Merge Sort
def merge_sort(arr):
    N = len(arr)
    if N <= 1:
        return arr
    else:
        mid = N//2
        return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def merge_sort_with_queue(arr):
    queue = Queue()
    if len(arr) <= 1:
        return arr
    for e in arr:
        queue.enqueue([e])
    while len(queue) > 1:
        arr1 = queue.dequeue()
        arr2 = queue.dequeue()
        queue.enqueue(merge(arr1, arr2))
    return queue.dequeue()

def merge(arr1, arr2):
    res = []
    i, j = 0, 0
    ln1, ln2 = len(arr1), len(arr2)
    while i<ln1 and j<ln2:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    if i < ln1:
        res += arr1[i:]
    else:
        res += arr2[j:]
    return res

# Quick Sort
def quick_sort(arr, stt, end):
    if stt < end:
        pivot = partition(arr, stt, end)
        quick_sort(arr, stt, pivot-1)
        quick_sort(arr, pivot+1, end)
    return arr

def quick_sort_with_queue(arr):
    queue = Queue()
    queue.enqueue(arr)
    while queue.length < len(arr):
        dq = queue.dequeue()
        len_dq = len(dq)
        if len_dq <= 1:
            queue.enqueue(dq)
            continue
        idx = partition(dq)
        if idx > 0:
            queue.enqueue(dq[:idx])
        queue.enqueue([dq[idx]])
        if idx < len_dq-1:
            queue.enqueue(dq[idx+1:])
    # 마지막 정렬
    ls = queue.dequeue()
    for i in range(queue.length-1):
        n = queue.dequeue()
        if ls[-1] > n[0] or queue.is_empty():
            break
        ls += queue.dequeue()
    ls2 = []
    for i in range(queue.length-1):
        if queue.is_empty():
            break
        ls2 += queue.dequeue()
    return ls2 + ls

def quick_sort_with_stack(arr):
    stack = Stack()
    stack.push((0, 0, 0, False))
    stt = 0; end = len(arr)-1;
    need_partition = True
    while True:
        if need_partition: # 처음 왔을 경우 / 둘 다 파티션 해야기에 왼쪽 먼저 파티션
            if stt < end:
                pivot = partition(arr, stt, end)
                stack.push((stt, end, pivot, False))
                end = pivot-1
                need_partition = True
                continue
            completed = True # 파티션 완료
        if not completed: # 왼쪽 파티션이 끝났지만 오른쪽 파티션이 안되었을 경우
            stack.push((stt, end, pivot, True))
            stt = pivot+1
            need_partition = True
            continue
        stt, end, pivot, completed = stack.pop()
        need_partition = False
        if stack.is_empty():
            break
    return arr

def partition(arr, stt, end):
    pivot = arr[stt] # 값
    j = stt
    for i in range(stt+1, end+1):
        if arr[i] < pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    pivot = j # 인덱스
    arr[stt], arr[pivot] = arr[pivot], arr[stt]
    return pivot