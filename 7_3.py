# Task_3

from os import path, walk, listdir
import shutil

new_project = 'my_project_1'

try:
    for root, dirs, files in walk(new_project):
        if 'templates' in dirs and root != new_project:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entry),
                                path.join(new_project, 'templates', entry))
except FileExistsError:
    print("Already worked with these templates!")
