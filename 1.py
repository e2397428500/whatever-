def rotode(intr):
    dict1 = {0:'',1:"I", 2:"II", 3:"III", 4:"IV", 5: "V", 6:"VI", 7: 'VII', 8:'VIII', 9: 'IX', 10: 'X'}# from one to 30.
    stri = ''
    if intr <= 10:
        for ro in dict1:
            if intr == ro:
                stri = dict1[ro]
                return stri
    else:
        intr -= 10
        for ro in dict1:
            if intr <= 10:
                stri = dict1[intr]
                return 'X' + stri
            else:
                if intr >10 and intr < 20: 
                    stri = dict1[intr]
                    return 'XX' + stri
                elif intr >= 20 and intr < 30:
                    intr -= 20
                    stri = dict1[intr]
                    return 'XXX' + stri
    # before 31, new trend for number above 30. 
            
            
        
  


        

        
            
        
    
    
