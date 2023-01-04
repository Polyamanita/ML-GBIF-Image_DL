import os
import shutil
import re

print('Working in', os.getcwd())

files = os.listdir()


for file in files:
    success = re.search('[a-zA-Z]*_[a-zA-Z]*_[0-9]*.jpg$', file)
    if success:
        split_file = file.split('_')
        new_dir = split_file[0] + '_' + split_file[1]
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
            print('Created new directory: ', new_dir)

        new_file = new_dir + '/' + file
        shutil.move(file, new_file)

        print('Moved', file, 'to', new_dir)

print('Successfully moved all files!')
