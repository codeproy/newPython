# calculate iterations to make a string plaindrome
import os
def  palindrome_calc(arg_str):
     for each_str in arg_str:
          dest_lst = list(each_str)
          i = 0
          s = 0
          j = len(each_str) - 1
          while i < j:
               ascii_i = ord(dest_lst[i])
               ascii_j = ord(dest_lst[j])
               if ascii_i > ascii_j:
                    s = s + (ascii_i - ascii_j)
               elif ascii_j > ascii_i:
                    s = s + (ascii_j - ascii_i)
               i = i + 1
               j = j - 1
          print(s)
     return
                      
def main():
     
     noofcase = int(input())
     arg_str = []
     while noofcase > 0:
          arg_str.append(input())
          noofcase = noofcase - 1
     palindrome_calc(arg_str)

main()

