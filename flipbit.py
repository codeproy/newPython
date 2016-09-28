# decimal to binary convesion, flipping the bits & throwing the decimal value)
def  flipbit(rcv):
    num = int(rcv)
    bin_num = ''

    while num > 0:
          bin_num = str(num % 2) + bin_num
          num = num // 2
    bin_num = (32-len(bin_num)) * '0' + bin_num

    list_num = list(bin_num)
    for i in range(0,len(list_num)):
        if int(list_num[i]) == 0:
            list_num[i] = 1
        elif int(list_num[i]) == 1:
            list_num[i] = 0

    rever_num = ''.join(str(l) for l in list_num)

    rever_int = int(rever_num, 2)
    return(rever_int)

no_of_input = int(input())
store_tbl = []
for subs in range(0,no_of_input):
    store_tbl.append(int(input()))

for subs in range(0,no_of_input):
        print(flipbit(store_tbl[subs]))
    
