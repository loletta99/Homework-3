# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:31:30 2019

@author: Rosa
"""

import os

def file_reader(file_name):
    path = ("./"+file_name)
    with open(path, "r") as file:
        s = file.read()
    return s.split("\n")[:-1]


if __name__== "__main__":
    l = file_reader("rosalind_med (2).txt")
    for el in l:
        print(el)
    print(len(l))

def median(a,k):
    b = sorted(a)
    return b[int(k)-1]

print(median(a,k))
