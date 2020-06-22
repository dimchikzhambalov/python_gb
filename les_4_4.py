src_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = []

for i in src_list:
    if i not in new_list:
        new_list.append(i)

print(src_list)
print(new_list)
