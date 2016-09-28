def round_dig(inp_num, inp_rnd):
        try:
                (mnts , decml) = str(inp_num).split(".")
                try:
                        decsv_num = int(decml[inp_rnd:inp_rnd+1])
                        if decsv_num > 5:
                                decml_int = int(decml[:inp_rnd]) + 1
                        else:
                                decml_int = int(decml[:inp_rnd])
                except:
                        decml_int = decml
                round_num = mnts + '.' + str(decml_int)
        except:
                round_num = inp_num
        print(round_num)
 
inp_num = input("Enter the number")
inp_rnd = int(input("Enter the rounding decimal"))
round_dig(inp_num,inp_rnd)
