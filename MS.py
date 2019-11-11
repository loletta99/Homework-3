#MS

def ms(ls):
    return sorted(ls)

with open("rosalind_ms (6).txt" , "r") as file:
    input_list = file.read().split("\n")
    string = input_list[1]
ls = list(map(int, string.split()))

result = ms(ls)
print (str(result).replace(",",""))