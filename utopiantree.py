# decimal to binary convesion, flipping the bits & throwing the decimal value)
def  utptree(rcv):
    num = int(rcv)
    div = num // 2
    rem = num % 2
    init_size = final_size = 1
    if rem == 0:
        while div > 0:
                final_size = 2 * init_size + 1
                init_size = final_size
                div = div - 1
    else:
        while div > 0:
                final_size = 2 * init_size + 1
                init_size = final_size
                div = div - 1
        final_size = 2 * init_size

    return(final_size)

no_of_input = int(input())
store_tbl = []
for subs in range(0,no_of_input):
    store_tbl.append(int(input()))

for subs in range(0,no_of_input):
        print(utptree(store_tbl[subs]))
    
