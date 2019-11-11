
#2sum
import os

def two_sum(A):
    # empty dictionary
    indices = {}

    # iterate through array elements
    for t in A:
        # check if 'opposite sign' exists in remainder
        if -A[t] in A[t+1:]:
            # check which element sums to zero
            for s in xrange(t+1, len(A)):
                if(A[t] + A[s] == 0):
                    # returns indices (+1 for Rosalind)
                    return [t+1, s+1]
                
    # loop failed so return -1
    return [-1]


if __name__ == '__main__':
    # read data
    with open("rosalind_2sum (1).txt" , "r") as file:
        k,n = file.readline().rstrip().split()
        data = ((int, line.strip().split()) for line in file.readlines())

        for d in data:
            print(" ".join(map(str, two_sum(d))))