def summm(i):
    lst = []
    si = sorted(i)
    for l in range(len(i)-2):
        a = si[l]
        m = l+1
        n = len(i)-1
        while m < n:
            b = si[m]
            c = si[n]
            if a+b+c == 0:
                lst.append(i.index(a)+1)
                lst.append(i.index(b)+1)
                lst.append(i.index(c)+1)
                return(sorted(lst))
            elif a+b+c > 0:
                n-=1
            elif a+b+c < 0:
                m+=1
    return [-1]

for line in open('rosalind_3sum.txt','r') :
    arr=list(map(int, line.split()))
    print ( *summm(arr) )