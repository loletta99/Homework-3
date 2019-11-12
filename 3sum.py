def sum3(i):
    lst3 = []
    si = sorted(i)
    for l in range(len(i)-2):
        a = si[l]
        m = l+1
        n = len(i)-1
        while m < n:
            b = si[m]
            c = si[n]
            if a+b+c == 0:
                lst3.append(i.index(a)+1)
                lst3.append(i.index(b)+1)
                lst3.append(i.index(c)+1)
                return(sorted(lst3))
            elif a+b+c > 0:
                n-=1
            elif a+b+c < 0:
                m+=1
    return [-1]
with open('rosalind_3sum.txt') as f:
    r = f.readline()
    arr=list(map(int,f.readline.split()))
    print ( *sum3(arr) )