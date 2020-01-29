def romanNum(x):
    #print("Roman!")

    roma = ""
    roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"] #list of roman numerals
    arabic = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] #arabic value of roman numeral
    i = 12 #number of values in the above arrays

    while x > 0: #while the number is greater than 0
        div = x // arabic[i] #find the quotient
        #print(div)
        x %= arabic[i] #get the remainder
        #print(x)

        while div > 0: #while the quotient is greater than 0
            roma = roma + roman[i]
            #print(roman[i], end = "") #print roman numeral digit
            div -= 1 #decrement the quotient

        i -= 1 #move to the next roman numeral digit

    return roma

def test_conversion():
    assert romanNum(3) == "III"