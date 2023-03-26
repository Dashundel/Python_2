# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# -   Для дочерних объектов указывайте родительскую директорию. 
# -   Для каждого объекта укажите файл это или директория.
# -   Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней 
#    с учётом всех вложенных файлов и директорий.

import csv
import json
from pathlib import Path
import pickle
import os

__all__ = ['recursionDir']

import os
from pathlib import Path
import csv
import json
import pickle

def getSizeDir(path: Path = '.') -> int:
    result = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += getSizeDir(entry.path)
    return result


def getSize(path: Path = '.') -> int:
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return getSizeDir(path)
		
		
def recursionDir(path: Path):
    jsonData = {}
    csvData = []
    field = ['name', 'path', 'size', 'type']

    for dir_path, dir_names, file_names in os.walk(path):
    
        jsonData.setdefault(dir_path, {})
        
        for dir_name in dir_names:
            size = getSize(dir_path + '/' + dir_name)
            jsonData[dir_path].update({dir_name: {'size': size, 'type': 'directory'}})
            csvData.append({'file': dir_name, 'path': dir_path, 'size': size, 'type': 'directory'})
            
        for file_name in file_names:
            size = getSize(dir_path + '/' + file_name)
            jsonData[dir_path].update({file_name: {'size': size, 'type': 'file'}})
            csvData.append({'file': file_name, 'path': dir_path, 'size': size, 'type': 'file'})

    with open('file.json', 'w', encoding = 'utf-8') as jsonf:
        json.dump(jsonData, jsonf, indent = 2)
        
    with open('file.csv', 'w', newline='', encoding = 'utf-8') as csvf:
        writer = csv.writer(csvf)
        writer.writerows(csvData)
        
    with open('file.pickle', 'wb') as picklef:
        pickle.dump(f'{pickle.dumps(jsonData)}', picklef)
       

if __name__ == '__main__':
    recursionDir(Path('D:\HM\python2\hw8\123.txt'))