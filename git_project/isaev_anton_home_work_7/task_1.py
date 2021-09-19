import os

ROOT = os.path.dirname(__file__)
dir_name = 'my_project'
paths = [os.path.join(dir_name, 'setting'), os.path.join(dir_name, 'mainapp'), os.path.join(dir_name, 'adminapp'),
         os.path.join(dir_name, 'authapp')]
for my_path in paths:
    os.makedirs(os.path.join(ROOT, my_path), exist_ok=True)
