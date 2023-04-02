# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных),которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.

import csv
import json
from pathlib import Path
import pickle
import os

__all__ = ['recursionDir']

class Serializer:
    def __init__(self, directory: Path):
        self.directory = directory

    def getSizeDir(self) -> int:
        result = 0
        with os.scandir(self.directory) as it:
            for entry in it:
                if entry.is_file():
                    result += entry.stat().st_size
                elif entry.is_dir():
                    result += getSizeDir(entry.path)
        return result


    def getSize(self) -> int:
        if os.path.isfile(self.directory):
            return os.path.getsize(self.directory)
        elif os.path.isdir(self.directory):
            return getSizeDir(self.directory)
            
            
    def recursionDir(self):
        jsonData = {}
        csvData = []
        field = ['name', 'path', 'size', 'type']

        for dir_path, dir_names, file_names in os.walk(self.directory):
        
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
    newfile = Serializer(directory = 'D:\HM\python2\hw8\123.txt') 
    newfile.recursionDir()

  