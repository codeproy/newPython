def avg_num(inp_arr , inp_no_elem):
        a = []
        a = list(inp_arr)
        s = 0
        for each_elem in a:
             s = s + each_elem
        out_avg = s / inp_no_elem
	return(out_avg)
		


inp_arr = input("Enter the number")
inp_no_elem input("enter the number of elem")
print(avg_num(inp_arr , inp_no_elem))



