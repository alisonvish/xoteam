import os
import shutil


def folders_sort(folder_path):
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()] #вложенный файл
    new_folders = []
