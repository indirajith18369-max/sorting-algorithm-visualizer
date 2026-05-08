
# Bubble Sort — O(n^2) time, O(1) space
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort — O(n^2) time, O(1) space
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if arr[j] < arr[m]: m = j
        arr[i], arr[m] = arr[m], arr[i]

# Insertion Sort — O(n^2) time, O(1) space
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key, j = arr[i], i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]; j -= 1
        arr[j+1] = key

# Merge Sort — O(n log n) time, O(n) space
def merge_sort(arr, l=0, r=None):
    if r is None: r = len(arr)-1
    if l < r:
        m = (l+r)//2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        L, R = arr[l:m+1], arr[m+1:r+1]
        i = j = 0; k = l
        while i < len(L) and j < len(R):
            if L[i] <= R[j]: arr[k] = L[i]; i += 1
            else: arr[k] = R[j]; j += 1
            k += 1
        while i < len(L): arr[k] = L[i]; i += 1; k += 1
        while j < len(R): arr[k] = R[j]; j += 1; k += 1

# Quick Sort — O(n log n) avg, O(log n) space
def quick_sort(arr, lo=0, hi=None):
    if hi is None: hi = len(arr)-1
    if lo < hi:
        p = arr[hi]; i = lo-1
        for j in range(lo, hi):
            if arr[j] < p: i += 1; arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[hi] = arr[hi], arr[i+1]
        quick_sort(arr, lo, i); quick_sort(arr, i+2, hi)

# Heap Sort — O(n log n) time, O(1) space
def heap_sort(arr):
    import heapq
    heapq.heapify(arr)
    arr[:] = [heapq.heappop(arr) for _ in range(len(arr))]

# Shell Sort — O(n^1.5) time, O(1) space
def shell_sort(arr):
    n = len(arr); gap = n//2
    while gap > 0:
        for i in range(gap, n):
            t, j = arr[i], i
            while j >= gap and arr[j-gap] > t:
                arr[j] = arr[j-gap]; j -= gap
            arr[j] = t
        gap //= 2

# Counting Sort — O(n+k) time, O(k) space
def counting_sort(arr):
    mx = max(arr); c = [0]*(mx+1)
    for v in arr: c[v] += 1
    i = 0
    for v in range(mx+1):
        for _ in range(c[v]): arr[i] = v; i += 1

# Radix Sort — O(d*n) time, O(n) space
def radix_sort(arr):
    mx = max(arr); exp = 1
    while mx // exp > 0:
        out = [0]*len(arr); c = [0]*10
        for v in arr: c[(v//exp)%10] += 1
        for i in range(1,10): c[i] += c[i-1]
        for v in reversed(arr): d=(v//exp)%10; out[c[d]-1]=v; c[d]-=1
        arr[:] = out; exp *= 10

# Tim Sort — O(n log n) time, O(n) space
def tim_sort(arr):
    arr.sort()  # Python's built-in sort IS Tim Sort
