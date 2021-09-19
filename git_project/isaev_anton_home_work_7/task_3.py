import os
from shutil import copy

root_dir = os.path.join(os.path.dirname(__file__), 'my_project')
dst_dir = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

for root, dirs, files in os.walk(root_dir):
    for dir1 in dirs:
        if not os.path.exists(os.path.join(dst_dir, dir1)):
            os.makedirs(os.path.join(dst_dir, dir1))
    for file in files:
        src_file = os.path.join(root, file)
        dst_file = os.path.join(dst_dir, os.path.basename(root))
        if not os.path.dirname(src_file) == dst_file:
            copy(src_file, dst_file)
