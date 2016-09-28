# calculate iterations to make a string plaindrome
import os
def  icrm_parlr(guys_money , parlr_items, parlr_price):
     parlr_price_each = parlr_price.split()
     result_indc = []
     m = 0
     cond_not_met = True
     print(len(parlr_price_each))
     while cond_not_met:
           print(1)
           for i in range(0,len(parlr_price_each) - 1):
               print(2)
               if int(parlr_price_each[i]) >= guys_money:
                    continue
               else:
                    for j in range(1, len(parlr_price_each)):
                         if guys_money == int(parlr_price_each[i]) + int(parlr_price_each[j]):
                              result_indc.append(str(i) + ',' + str(j))
                              cond_not_met = False
     print(result_indc[0])
     return
                      
def main():
     
     noofcase = int(input())
     arg_str = []
     for i in range(0 , noofcase * 3):
          guys_money = int(input())
          parlr_items = input()
          parlr_price = input()
          icrm_parlr(guys_money , parlr_items, parlr_price)

main()
