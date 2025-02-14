#!/usr/bin/env python3
# Author ID: [161112214]

def read_file_string(file_name):
    file = open(file_name, "r")
    return file.read()
    file.close()    

def read_file_list(file_name):
    file = open(file_name, "r")
    newList = [] 
    for line in file:
        newLine = line.strip()
        newList.append(newLine)
    return newList

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))