# decimal to binary convesion, flipping the bits & throwing the decimal value)
num = int(input('enter the number for binary conversion'))
bin_num = ''

while num > 0:
          bin_num = str(num % 2) + bin_num
          num = num // 2
print (bin_num)
print (len(bin_num))
bin_num = (32-len(bin_num)) * '0' + bin_num
print (bin_num)

list_num = list(bin_num)
for i in range(0,len(list_num)):
    if int(list_num[i]) == 0:
        list_num[i] = 1
    elif int(list_num[i]) == 1:
        list_num[i] = 0

rever_num = ''.join(str(l) for l in list_num)
print(rever_num)

rever_int = int(rever_num, 2)

print("rever_int" , rever_int)
