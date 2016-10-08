def replaceLinkList(head, tdata, rdata):
    shead = head
#   found = False
    while(head != None):
        if(head.data == tdata):
            head.data = rdata
        head = head.nexti
    
        
    return (shead)


              
