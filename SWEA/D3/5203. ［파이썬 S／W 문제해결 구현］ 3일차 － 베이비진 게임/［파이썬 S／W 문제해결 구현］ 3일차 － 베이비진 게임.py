T = int(input())
def babygin(cnt):
    i = 0
    while i != 11:
        if cnt[i] >= 3:
            return 'triplet'
        elif cnt[i] >= 1 and cnt[i+1]>= 1 and cnt[i+2]>=1:
            return 'run1'
        else:
            i += 1
    else: return 0


for t in range(1,T+1):
    arr = list(map(int,input().split()))
    player1 = []
    player2 = []
    for i in range(0,len(arr),2):
        player1.append(arr[i])
    for i in range(1,len(arr),2):
        player2.append(arr[i])

    cnt1 = [0] * 12
    cnt2 = [0] * 12
    for i in range(6):
        cnt1[player1[i]] += 1
        cnt2[player2[i]] += 1

        if babygin(cnt1):
            print(f"#{t} 1")
            break
        elif babygin(cnt2):
            print(f'#{t} 2')
            break

    if babygin(cnt1) == 0 and babygin(cnt2)==0:
        print(f'#{t} 0')