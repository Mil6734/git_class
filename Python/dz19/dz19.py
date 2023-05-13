import os

dir_main = r'C:\pythonMy\myProject\git_class\dz19\home_work'

for i in os.listdir(dir_main):
    if os.path.isdir(dir_main + f'\\{i}'):
        print(f'{i} - dir')
    elif os.path.isfile(dir_main + f'\\{i}'):
        print(i, '- file -', os.path.getsize(dir_main + f"\\{i}"), 'byte')
