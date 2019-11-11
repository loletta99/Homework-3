#mer
def merg(arrayc):
    return(sorted(arrayc))
with open("rosalind_mer (4).txt" , "r") as file:
    input_list = file.read().split("\n")
    string, to_find_string = input_list[1], input_list[3]
    arraya= list(map(int,string.split()))
    arrayb= list(map(int,to_find_string.split()))
    arrayc = list(arraya + arrayb)
    result = merg(arrayc)
print(str(result).replace(",",""))