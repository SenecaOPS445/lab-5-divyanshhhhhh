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

def append_file_string(file_name, string_of_lines):
    file = open(file_name, "a")
    newFile = file.write(string_of_lines)
    file.close()
    return newFile

def write_file_list(file_name, list_of_lines):
    file = open(file_name, "w")
    for eachLine in list_of_lines:
        newFile = file.write(eachLine + '\n')
    file.close()
    return newFile

def copy_file_add_line_numbers(file_name_read, file_name_write):
    file = open(file_name_read, "r")
    newFile = open(file_name_write, "w")
    lineNumber = 1
    for line in file:
        newLine = str(lineNumber) + ':' + line
        newFile.write(newLine)
        lineNumber = lineNumber + 1
    file.close()
    newFile.close()
    return newFile


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))