def get_result(ans, key):
    if ans == "OOOO":
        return 0
    
    if key == "A":
        if ans == "#OOO":
            return 1
        else: 
            return -1
    
    if key == "B":
        if ans == "O#OO":
            return 1
        else: 
            return -1
        
    if key == "C":
        if ans == "OO#O":
            return 1
        else: 
            return -1
        
    if key == "D":
        if ans == "OOO#":
            return 1
        else: 
            return -1
        
n = int(input())

keys = input()

k = int(input())

for i in range(0,k):
    true_num = 0
    false_num = 0
    for j in range(0,n):
        ans = input()

        result = get_result(ans, keys[j])
        if( result == 1 ):
            true_num += 1
        elif( result == -1):
            false_num += 1
    
    print(3*true_num-false_num)