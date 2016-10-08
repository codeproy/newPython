def searchLinkList(head, probe):
#   found = False
    while((head != None) and (probe != head.data)):
            head = head.nexti
    if (head != None):
        return(True)
    else:
        return(False)
          
