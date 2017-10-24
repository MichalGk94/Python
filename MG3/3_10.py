def roman2int(roman):
    arabic = 0
    for i in range(len(roman)):
        if roman[i] == 'M':
            if i-1 > -1 and roman[i-1] == 'C':
                arabic += 900
            else: arabic += 1000
        elif roman[i] == 'D':
            if i-1 > -1 and roman[i-1] == 'C':
                arabic += 400                
            else: arabic += 500
        elif roman[i] == 'C':
            if i-1 > -1 and roman[i-1] == 'X':
                arabic += 90                
            elif i+1 < len(roman)-1 and roman [i+1] != 'M' and roman[i+1] != 'D':
                arabic += 100
        elif roman[i] == 'L':
            if i-1 > -1 and roman[i-1] == 'X':
                arabic += 40                
            else: arabic += 50
        elif roman[i] == 'X':
            if i-1 > -1 and roman[i-1] == 'I':
                arabic += 9                
            elif i+1 < len(roman)-1 and roman[i+1] != 'C' and roman[i+1] != 'L':
                arabic += 10
        elif roman[i] == 'V':
            if i-1 > -1 and roman[i-1] == 'I':
                arabic += 4                
            else: arabic += 5
        elif roman[i] == 'I': 
            if i+1 < len(roman)-1 and romn[i+1] != 'X' and roman[i+1] != 'V':
                arabic += 1
    return arabic

D = dict()
D['I'] = 1
D['V'] = 5
D['X'] = 10
D['L'] = 50
D['C'] = 100
D['D'] = 500
D['M'] = 1000

print D.items()

roman = raw_input("Podaj liczbe rzymska: ")
arabic = roman2int(roman)
print arabic
