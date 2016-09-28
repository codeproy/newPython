# finding max car size that can pass thru the exits
def  carlane(frway , width, entry_exit):
     for indx in range(0 , len(entry_exit), 2) :
          sub1 = int(entry_exit[indx])
          sub2 = int(entry_exit[indx + 1]) + 1
          min_width = min(width[sub1 : sub2])
          print(min_width)
            
frway_parm = input().split()
width_parm = input().split()
test_num = int(frway_parm[1])
i = 0
entry_exit_parm = []
while test_num > 0:
     entry_exit_parm.extend(input().split())
     test_num = test_num - 1
carlane(frway_parm, width_parm, entry_exit_parm)
