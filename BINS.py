#bins
def bins(lst1,lst2):
    lsti = []
    for n in lst2:
        if n in lst1:
            s = lst1.index(n)
            lsti.append(s+1)
        elif n not in lst1:
            lsti.append(-1)
    return lsti
with open("rosalind_bins.txt" , "r") as file:
    input_list = file.read().split("\n")
    string, to_find_string = input_list[2], input_list[3]
    lst1= list(map(int,string.split()))
    lst2= list(map(int,to_find_string.split()))
    result = bins(lst1,lst2)
print(str(result).replace(",",""))