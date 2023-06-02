import os
import shutil


def folders_sort(folder_path):
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()] #вложенный файл
    new_folders = []
    for i in range(1, 11):
        new_folder_path = os.path.join(folder_path, str(i) + '_new')
        os.makedirs(new_folder_path)
        new_folders.append(new_folder_path)
    for subfolder in subfolders:
        files = os.listdir(subfolder)
        files.sort()
