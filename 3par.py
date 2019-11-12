# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:50:32 2019

@author: Rosa
"""

from file_reader import file_reader
#par

def part(arr):
    i = len(arr)-1
    p = arr[0]
    for j in range(len(arr)-1, 0, -1):
        if arr[j] > p:
            arr[j], arr[i] = arr[i],arr[j]
            i -= 1
    arr[i], arr[0] = arr[0],arr[i]
    i -=1
    for j in range(i, -1, -1):
        if arr[j] == p:
            arr[j], arr[i] = arr[i], arr[j]
            i -= 1
    return arr

if __name__ == "__main__":
    input_list = file_reader("rosalind_par3.txt")
    s = [4,5,6,4,1,2,5,7,4]
    array = list(map(int, input_list[1].split()))
    part(array)
    par(s)
    print(s)
    answer = " ".join(list(map(str, array)))
    print(answer)
    with open("./answer1.txt", "w") as file:
        file.write(answer)