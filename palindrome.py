# calculate iterations to make a string plaindrome
import os
def  palindrome_calc(inp_str):
     print("inp_str", inp_str)
     dest_lst = list(inp_str)
     i = 0
     j = len(inp_str) - 1
     while i < j:
          ascii_i = ord(inp_str[i])
          ascii_j = ord(inp_str[j])
          if ascii_i > ascii_j:
               ascii_i = reduce_ascii(ascii_i , ascii_j)
               print("ascii_iireturn",ascii_i)
               dest_lst[i] = chr(ascii_i)
          elif ascii_j > ascii_i:
               ascii_j = reduce_ascii(ascii_j , ascii_i)
               print("ascii_jreturn",ascii_j)
               dest_lst[j] = chr(ascii_j)
          print("dest_list", dest_lst)
          i = i + 1
          j = j - 1
     return(dest_lst)
          

def reduce_ascii(source_val, dest_val):
     while source_val > dest_val:
               source_val = source_val - 1
     return(source_val)
            
def main():
     
     noofcase = int(input())
     while noofcase > 0:
          arg_str = input()
          print(arg_str)
          noofcase = noofcase - 1
          print(palindrome_calc(arg_str))

main()

