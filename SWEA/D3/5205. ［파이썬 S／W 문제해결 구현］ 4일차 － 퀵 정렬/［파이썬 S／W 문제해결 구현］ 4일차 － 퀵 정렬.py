def hoare_partition(arr,low,high):
    pivot = arr[(low+high)//2]
    i,j = low,high
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1

def quick_sort(arr,low,high):
    if low < high:
        p = hoare_partition(arr,low,high)
        quick_sort(arr,low,p)
        quick_sort(arr,p+1,high)

T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    quick_sort(arr,0,N-1)
    print(f"#{t} {arr[len(arr)//2]}")