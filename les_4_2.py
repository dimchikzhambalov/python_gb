scr_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
for i in range(1, len(scr_list) - 1):
    if scr_list[i] < scr_list[i+1]:
        new_list.append(scr_list[i+1])
    i += 1

print(scr_list)
print(new_list)
