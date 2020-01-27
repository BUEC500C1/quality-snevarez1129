print("Hello, welcome to my converter!")

def romanNum(x):
    print("Roman!")

    roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"] #list of roman numerals
    arabic = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] #arabic value of roman numeral
    i = 12 #number of values in the above arrays

    return 2

def main():
    arab = int(input("Please enter an arabic number: ")) #accept user input of an arabic number
    #print("The Arabic Number = ", arab)
    #print("The type is = ", type(arab))

    roma = romanNum(arab) #call conversion function
    print("The Roman Numeral = ", roma) #print the converted roman numeral
    #print("The type is = ", type(roma))
    
    print("Thanks for playing! Goodbye!") #exit program

if __name__ == "__main__":
    main()
