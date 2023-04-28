inp = input()

zero_num = 0
one_num = 0
state = 0

result = True

for i in range(0, len(inp)):
    if state == 0:
        if inp[i] == '0':
            zero_num += 1
        else:
            state = 1
            one_num = 1
    else:
        if inp[i] == '0':
            state = 0

            if zero_num != one_num:
                result = False
                break

            zero_num = 1
            one_num = 0
        else:
            one_num += 1

if zero_num != one_num:
    result = False

if result == False:
    print("False")
else : print("True")