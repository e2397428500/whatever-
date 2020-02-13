def rotode(intr):
    dict1 = {0:'',1:"I", 2:"II", 3:"III", 4:"IV", 5: "V", 6:"VI", 7: 'VII', 8:'VIII', 9: 'IX', 10: 'X'}# from one to 30.
    stri = ''
    if intr <= 10:
        for ro in dict1:
            if intr == ro:
                stri = dict1[ro]
                return stri
    elif intr > 10 and intr < 40:
        intr -= 10
        for ro in dict1:
            if intr <= 10:
                stri = dict1[intr]
                return 'X' + stri # for 20 and above 
            else:
                if intr >10 and intr < 20: 
                    stri = dict1[intr]
                    return 'XX' + stri
                elif intr >= 20 and intr < 30:
                    intr -= 20
                    stri = dict1[intr]
                    return 'XXX' + stri # for 30 and above 
    elif intr >= 40:
        return above40(intr)
    elif intr == 100:
        return 'C' 
def above40(intr):
    dict2 = {40:"XL" , 50:"L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC"}
    str2 = '' # single digit
    if intr >= 40:
        for ro in dict2:
            str3 = intr - ro
            if str3 < 10:
                single = rotode(str3)
                str2 = dict2[ro]
                call = str2 + single
                return call
            
            
            
        

    
    


            
            
        
  


        

        
            
        
    
    
