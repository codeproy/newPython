# calculate iterations to make a string plaindrome
import os
def  strng_del(arg_str):
     for each_str in arg_str:
          prev_elem = ''
          del_count = 0
          for each_elem in each_str:
               if each_elem == prev_elem:
                    del_count = del_count + 1
               else:
                    prev_elem = each_elem
          print(del_count)
     return
                      
def main():
     
     noofcase = int(input())
     arg_str = []
     while noofcase > 0:
          arg_str.append(input())
          noofcase = noofcase - 1
     strng_del(arg_str)

main()

