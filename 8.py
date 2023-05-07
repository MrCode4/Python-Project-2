n, m = input().split()

n = int(n)
m = int(m)

if(9*n < m or m < 1):
    print(-1, -1)
 
else :
    min_list = ['0' for i in range(n)]
    min_list[0] = '1'

    sum = m-1
    index = n-1

    for i in range(n-1, -1, -1):
        if sum <= 9:
            min_list[i] = str(int(min_list[i]) + sum)
            break
        else:
            min_list[i] = '9'
            sum -= 9

    min_value = "".join(min_list)

    max_list = ['0' for i in range(n)]
    sum = m

    for i in range(n):
        if(sum<=9):
            max_list[i] = str(sum)
            break
        else:
            max_list[i] = '9'
            sum -= 9

    max_value = "".join(max_list)

    print(max_value, min_value)
