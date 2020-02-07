def romanNum(x):

    roma = "" #string to be returned
    roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"] #list of roman numerals
    arabic = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] #arabic value of roman numeral
    i = 12 #number of values in the above arrays

    if x > 3999 or x < 1:
        roma = "Unavailable"
    else:
        while x > 0: #while the number is greater than 0
            div = x // arabic[i] #find the quotient
            x %= arabic[i] #get the remainder

            while div > 0: #while the quotient is greater than 0
                roma = roma + roman[i]
                div -= 1 #decrement the quotient

            i -= 1 #move to the next roman numeral digit

    return roma

def test_conversion():
    assert romanNum(-7) == "Unavailable"
    assert romanNum(0) == "Unavailable"
    assert romanNum(3) == "III"
    assert romanNum(12) == "XII"
    assert romanNum(27) == "XXVII"
    assert romanNum(32) == "XXXII"
    assert romanNum(45) == "XLV"
    assert romanNum(57) == "LVII"
    assert romanNum(69) == "LXIX"
    assert romanNum(77) == "LXXVII"
    assert romanNum(88) == "LXXXVIII"
    assert romanNum(93) == "XCIII"
    assert romanNum(139) == "CXXXIX"
    assert romanNum(295) == "CCXCV"
    assert romanNum(302) == "CCCII"
    assert romanNum(471) == "CDLXXI"
    assert romanNum(523) == "DXXIII"
    assert romanNum(680) == "DCLXXX"
    assert romanNum(764) == "DCCLXIV"
    assert romanNum(818) == "DCCCXVIII"
    assert romanNum(907) == "CMVII"
    assert romanNum(1054) == "MLIV"
    assert romanNum(2309) == "MMCCCIX"
    assert romanNum(3459) == "MMMCDLIX"
    assert romanNum(6278) == "Unavailable"
    #assert romanNum('i') == "Unavailable" => Verifying user enters an int happens in main function
    #assert romanNum("hello") == "Unavailable"
    #assert romanNum(59.44444) == "Unavailable"
