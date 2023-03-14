def binary_search(arr, start, end, target):
    if end >= start:
        mid = start + end - 1 // 2

        if arr[mid] < target:
            binary_search(arr, mid+1, end, target)
        elif arr[mid] > target:
            return binary_search(arr, start, mid-1, target)
        else: return mid
    else: return -1

arr = [2,5,8,10,16,22,25]

result = binary_search(arr, 0, len(arr), 10)

print(str(result))