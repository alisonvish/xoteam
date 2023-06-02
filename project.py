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
        for i, file in enumerate(files):
            file_path = os.path.join(subfolder, file)
            new_file_name = os.path.basename(subfolder) + '_' + file
            new_file_path = os.path.join(new_folders[i], new_file_name)
            shutil.copy2(file_path, new_file_path) 
        shutil.rmtree(subfolder)
        
arr = ['А', 'Б', 'В', 'Г']

for it in arr:
    folders_sort(it)
