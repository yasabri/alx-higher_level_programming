#!/usr/bin/python3
""" Module with a method for reading data from a file """


def read_file(filename=""):
    """ Function  reads from  file"""

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
