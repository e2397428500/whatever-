## this function convert digit to roman number from range(1 to 1000)


def digits(intr):
    if intr < 10:
        return single(intr)
    if intr >= 10 and intr < 100:
        return aboveten(intr)
    if intr >= 100 and intr <= 1000:
        return abovehun(intr) 

def single(intr):
    dict1 = {0:'',1:"I", 2:"II", 3:"III", 4:"IV", 5: "V", 6:"VI", 7: 'VII', 8:'VIII', 9: 'IX'}# from one to 30. SINGLE DITS FUNCTION
    stri = ''
    for ro in dict1:
        if intr == ro:
            stri = dict1[ro]
            return stri
def aboveten(intr):
    dict2 = {10:"X", 20: "XX", 30:"XXX", 40:"XL" , 50:"L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC"}
    str2 = '' # single digit
    for ro in dict2:
        str3 = intr - ro
        if str3 < 10:
            sin= single(str3)
            str2 = dict2[ro]
            call = str2 + sin
            return call

def abovehun(intr):
    dict3 = {100:"C",200:"CC", 300: "CCC", 400:"CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM", 1000: "M"}
    str1 = ''
    for ro in dict3:
        str2 = intr - ro
        if str2 < 100 and str2 >= 10:
            sin = aboveten(str2)
            str1 = dict3[ro]
            call = str1 + sin
            return call
        elif str2 < 100 and str2 <= 10:
            sin = single(str2)
            str1 = dict3[ro]
            call = str1 + sin
            return call
        
    
##call = int(input("Pls enter a integer from 1 to 1000: "))
##print(digits(call))

        

        
            
        
    
    
