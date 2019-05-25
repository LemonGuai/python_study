with open('random.txt', 'r') as file:
    text = file.readlines()
item_list = [num.strip() for num in text]
# print(item_list)
set_list = set(item_list)
count_list = []
for i in set_list:
    count = item_list.count(i)
    count_list.append(count)

max_count = max(count_list)
print(item_list)
print(set_list)
print(max_count)
print(count_list)
