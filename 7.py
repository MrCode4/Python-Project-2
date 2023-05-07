print(*sorted([int(num) for index, num in enumerate(input().split(), start=1) if int(num) % 6 == 0 and index % 6 == 0 ]), sep= '\n')
