import sys

def dec2bin(val):
    intVal = int(val)
    ans = ""
    while(intVal > 0):
        ans = str(intVal % 2) + ans #append backward
        intVal = intVal // 2
    return ans

def bin2dec(val):
 # val is a string of 1’0 and 0’s
 # I will interpret a positive integer
    ans = 0
    exp = len(val) - 1
    for digit in val:
        if(digit == "1"):
            ans = ans + 2**exp
            exp = exp - 1
    return int(ans)

def dec2hex(val):
    intVal = int(val)
    ans = ""
    while (intVal > 0):
        remainder = intVal % 16
        ans = remainderDec2Hex(remainder) + ans
        intVal = intVal // 16
        
    return "0x" + (ans if ans != "" else "0")

def hex2dec(val):
    # val is a string

    # create a dictionary to hold corresponding values
    table = {'0': 0, '1': 1, '2': 2, '3': 3,  
         '4': 4, '5': 5, '6': 6, '7': 7, 
         '8': 8, '9': 9, 'A': 10, 'B': 11,  
         'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    ans = 0
    exp = len(val) - 1
    for charDig in val:
        ans = ans + table[charDig] * 16**exp 
        exp = exp - 1 # go down in units of 16-base exponentials
    ans = str(ans)
    return ans # ref: chatGPT - this ensure the correct format for non-empty values in hexadecimal

def bin2hex(val):
    ans = dec2hex(bin2dec(val))

def hex2bin(val):
    return dec2bin(hex2dec(val))
        
def remainderDec2Hex(rem):
    if rem >= 0 and rem <= 9:
        return str(rem)
    elif rem == 10:
        return("A")
    elif rem == 11:
        return("B")
    elif rem == 12:
        return("C")
    elif rem == 13:
        return("D")
    elif rem == 14:
        return("E")
    else: 
        return("F")


def main():
    inputVal = sys.argv[1] # (val) eg. 25 or BE23
    ogFormat = sys.argv[2] # original format of the value
    goalFormat = sys.argv[3] # format to which the value is to be converted

    if ogFormat.lower().__eq__("d"):  
        if goalFormat.__eq__("d"):
            print(inputVal)
        elif goalFormat.__eq__("b"):
            print(dec2bin(inputVal))
        elif goalFormat.__eq__("h"):
            print(dec2hex(inputVal))
    elif ogFormat.lower() == "b":
        if goalFormat.__eq__("b"):
            print(inputVal)
        elif goalFormat == "d":
            print(bin2dec(inputVal))
        elif goalFormat == "h":
            print(bin2hex(inputVal))
    elif ogFormat.lower() == "h":
        if goalFormat == "h":
            print("0x" + (inputVal if inputVal != "" else "0"))
        elif goalFormat == "b":
            print(hex2bin(inputVal))
        elif goalFormat == "d":
            print(hex2dec(inputVal))

    

if __name__ == "__main__":
    main()
