print("Hello, welcome to my converter!")

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

def main():

    cont = 'y'

    while cont == 'y':
        arab = int(input("To begin, please enter an arabic number: ")) #accept user input of an arabic number
        #print("The Arabic Number = ", arab)
        #print("The type is = ", type(arab))

        numeral = romanNum(arab) #call conversion function
        print("The Roman Numeral for", arab, "is: ", numeral)
        #print("The Roman Numeral = ", roma) #print the converted roman numeral
        #print("The type is = ", type(roma))

        cont = input("nWould you like to enter a new number? [y/n]: ")
    
    print("Thanks for playing! Goodbye!") #exit program

if __name__ == "__main__":
    main()
