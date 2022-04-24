import os
import bojmaker
who_path = '/Users/jehyeonan/PS/2022-04/'
dir_list=[]
tmp = os.listdir(who_path)
for item in tmp:
    if '.py' in item:
        dir_list.append(item)
dir_list.sort()
for item in dir_list:
    print(item)
    item_path = os.path.join(who_path, item)
    file_name = item.replace('.py', '')
    file_num = file_name[3:]
    new_item_path = os.path.join(who_path, file_name, item)
    bojmaker.bojmaker(file_num)
    os.system(f'cat {item_path} >> {new_item_path}')
    os.system(f'rm {item_path}')