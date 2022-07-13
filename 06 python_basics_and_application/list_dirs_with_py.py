import os

dirs_list = []

for current_dir, dirs, files in os.walk('main'):
    for file in files:
        if file.endswith('.py'):
            dirs_list.append(current_dir)
            break

with open('dirs.txt', 'w') as fo:
    fo.write('\n'.join(sorted(dirs_list)))
