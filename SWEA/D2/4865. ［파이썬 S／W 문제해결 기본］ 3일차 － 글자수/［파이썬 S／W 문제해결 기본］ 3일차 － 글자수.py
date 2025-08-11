T = int(input())

for t in range(1,T+1):
    str1 = list(input())
    str2 = list(input())

    count_list = []

    for i in range(len(str1)):
        count = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count += 1
        count_list.append(count)
    print(f"#{t} {max(count_list)}")
