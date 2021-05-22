def max_num(inp_arr):
        max_elem = 0
        count_elem = 0
        max_coun = 0
        for each_elem in inp_arr:
             if each_elem == prev_elem:
                     count_elem = count_elem + 1
             else:
                  if count_elem > max_count:
                          max_count = count_elem
                          max_elem = each_elem
                  else:
                      count_elem = 0
        return(max_elem)

# added a comment 
		
inp_arr = input("Enter the number")
print(max_num(inp_arr))



