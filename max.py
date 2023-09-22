list1 = [1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 6]

dict_cnt = {} 

for i in list1:
    if i in dict_cnt:
        dict_cnt[i] += 1
    else:
        dict_cnt[i] = 1


number = None
max_count = 0
for i, count in dict_cnt.items():
    if count > max_count:
        number = i
        max_count = count

print(f"Number with highest count is : {number}")
