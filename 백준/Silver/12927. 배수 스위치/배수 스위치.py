arr = list(input())
cnt = 0
for i in range(len(arr)):
    if arr[i] == 'Y':
        for j in range(i,len(arr),i+1):
            if arr[j] == 'Y':
                arr[j] = 'N'
            else: arr[j] = 'Y'
        cnt += 1

        if 'Y' not in arr:
            break

print(cnt)