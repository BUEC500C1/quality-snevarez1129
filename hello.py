print("Hello, welcome to my converter!")

def romanNum(x):

    roma = "" #string to be returned
    roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"] #list of roman numerals
    arabic = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] #arabic value of roman numeral
    i = 12 #number of values in the above arrays

    if x > 3999 or x < 1:
        roma = "Unavailable" #converter can only handle numbers between 1 and 3999
    else:
        while x > 0: #while the number is greater than 0
            div = x // arabic[i] #find the quotient
            x %= arabic[i] #get the remainder

            while div > 0: #while the quotient is greater than 0
                roma = roma + roman[i]
                div -= 1 #decrement the quotient

            i -= 1 #move to the next roman numeral digit

    return roma

def main():

    cont = 'y'
    while cont == 'y':
        arab = input("To begin, please enter an arabic number: ") #accept user input of an arabic number

        try:
            int(arab)
        except ValueError:
           print("That's not an int!")
           usr_type = "string"
           while usr_type != "int":
               arab = input("Please enter an arabic number: ")
               try:
                   int(arab)
                   usr_type = "int"
               except ValueError:
                   print("No...")


        arab = int(arab)
        numeral = romanNum(arab) #call conversion function
        if numeral == "Unavailable":
            print("This converter can only handle arabic numbers between 1 and 3999. Please enter a different number.")
        else:
            print("The Roman Numeral for", arab, "is:", numeral)
        cont = input("nWould you like to enter a new number? [y/n]: ")
    
    print("Thanks for playing! Goodbye!") #exit program

if __name__ == "__main__":
    main()
