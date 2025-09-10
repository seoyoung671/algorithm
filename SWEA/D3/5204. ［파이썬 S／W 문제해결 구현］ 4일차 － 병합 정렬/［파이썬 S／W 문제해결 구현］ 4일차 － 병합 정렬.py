def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    cnt = 0
    result = merge_sort(arr)
    print(f"#{t} {result[len(result)//2]} {cnt}")