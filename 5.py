n = int(input())

dic = {}

for i in range(n):
    list = input().split()
    size = len(list)

    Item_Name = ""
    Item_Calories = int(list[size-3])
    Item_Fat = int(list[size-2])
    ISIRI_Sign = list[size-1]

    for i in range(0, size-3):
        if Item_Name == "":
            Item_Name = list[i]
        else:
            Item_Name = Item_Name + " " + list[i]

    if( ISIRI_Sign == "YES" and Item_Calories <= 100 and Item_Fat <= 50):
        if Item_Name in dic : 
            dic[Item_Name] += 1
        else:
            dic[Item_Name] = 1

sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

print(sorted_dic)