# find the maxim occur
input_no_elem = int(input("Enter the number of maximum elements "))
elem_table = []
elem_table = (input("enter the occurence")).split()
max_elem = 0  # maximum no. of ocuuernce
count_elem = 0 # sum of occurences
srch_table = [] # table for already searched elements

for i in range(0,input_no_elem):
        srch_elem = elem_table[i]
        count_elem = 0
        
        for j in range(0, input_no_elem):
                if srch_elem == elem_table[j]:   
                        count_elem = count_elem + 1

        else:
                if count_elem > max_elem :
                        max_elem = count_elem


print (" max occur", max_elem)


