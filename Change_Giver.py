Denominations = {1:[2000,500,200,100,50,20,10,5,2,1],2:[100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01],3:[50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01],4:[10000,5000,2000,1000,500,100,50,10,5,1],5:[100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]}
def checkval(s):
    while(True):
        value = input("-->  Enter the amount you wish to obtain the equivalent change for: ")
        try:
            value = float(value)
            if value < 0:
                print(".\n"*3)
                print(" ERROR !!! YOU HAVE ENTERED A NEGATIVE VALUE !!! PLEASE TRY AGAIN !!!")
            else:
                low_val_check = min(Denominations[s])
                if value<=low_val_check:
                    print(".\n"*3)
                    print(" ERROR !!! LOWER DENOMINATION DOES NOT EXIST, PLEASE ENTER A VALUE FOR WHICH CHANGE CAN BE OBTAINED !!!")
                else:
                    if s == 1 or s == 4:
                        print("\nYour Number Might be Rounded to the nearest integer due to Notes existing only in integer formats given the chosen currency. . . . ")
                        return round(value)
                    elif s == 2 or s==3 or s==5 :
                        print("\nYour Number Might be Rounded to 2 decimal places due to Notes existing only in integer formats given the chosen currency. . . . ")
                        return round(value,2)
        except ValueError:
            print(".\n"*3)
            print("YOUR ENTRY HAS INVALID CHARACTERS IN IT !!! PLEASE ENTER A NUMERICAL AMOUNT !!!")

def checkcurr(s):
    while(True):
        try:
            s = int(s)
            if 1<=s<=5:
                return s
            else:
                print(".\n"*3)  
                print("ERROR !!! NUMBER NOT IN SPECIFIED RANGE !!! PLEASE TRY AGAIN !!! \n")
                s = input("Enter The Numerical Value for your desired currency: ")
        except ValueError:
            print(".\n"*3)
            print("ERROR !!! ENTRY CONTAINS INVALID CHARACTERS !!! PLEASE TRY AGAIN !!! \n")
            s = input("Enter The Numerical Value for your desired currency: ")

def calc_change(c,a):
    list_of_denominations = Denominations[c]
    string = "Your Change is :"
    flag = 0
    for i in list_of_denominations:
        if a!=i:
            flag = 1
        if a >= i and flag == 1:
            part_of_change = int(a/i)
            part_of_change = str(part_of_change)
            a = a%i
            if c == 1:
                if i > 5:
                    string += " ' "+part_of_change+"'  "+str(i)+'  Rupee Note/s'
                else:
                    string += " ' "+part_of_change+"'  "+str(i)+'  Rupee Coin/s'
            elif c== 4:
                if i >= 1000:
                    string += " ' "+part_of_change+"'  "+str(i)+'  Yen Note/s'
                else:
                    string += " ' "+part_of_change+"'  "+str(i)+'  Yen Coin/s'
            elif c== 2:
                if i >= 1:
                    string += " ' "+part_of_change+"'  "+str(i)+'  Dollar Note/s'
                elif i == 0.01:
                    temp = int(i*100)
                    string += " ' "+part_of_change+"'  "+str(temp)+'  Penny/ies'
                elif i == 0.05:
                    temp = int(i*100)
                    string += " ' "+part_of_change+"'  "+str(temp)+'  nickel/s'
                elif i == 0.1:
                    temp = int(i*100)
                    string += " ' "+part_of_change+"'  "+str(temp)+'  Dime/s'
                elif i==0.25:
                    temp = int(i*100)
                    string += " ' "+part_of_change+"'  "+str(temp)+'  Quarter/s'
                elif i==0.5:
                    temp = int(i*100)
                    string += " ' "+part_of_change+"' "+str(temp)+'Half Dollar/s'
            elif c == 3:
                if i >= 5:
                    string += "' "+part_of_change+"'  "+str(i)+'  Pound Note/s'
                elif i==2 or i == 1:
                    string += " ' "+part_of_change+"'  "+str(i)+'  Pound Coin/s'
                else:
                    string += " ' "+part_of_change+"'  "+str(i)+'  Pence'
            else:
                if i >= 0.1:
                    temp = int(i*100)
                    string += " ' "+part_of_change+"'  "+str(temp)+'  Yuan Note/s'
                else:
                    temp = int(i*100)
                    string += " ' "+part_of_change+"'  "+str(temp)+'  Yuan Coin/s'
    return string


def main():
    ans = 'y'
    while(ans == 'y'):
        print(" "*10+"*-"*35+"*")
        print(" "*35+"COIN CHANGE MAKER")
        print(" "*10+"*-"*35+"*","\n")
        print("-->  Choose the NUMERICAL VALUE corresponding to the currency you wish to obtain the change in :\n1) Indian Rupee (₹) \n2) American Dollar ($) \n3) British Pound (£) \n4) Japanese Yen (¥) \n5) Chinese Yuan (CN¥) \n")
        int_value = input("Enter The Numerical Value for your desired currency: ")
        currency = checkcurr(int_value)
        print(".\n"*3)
        print("OPTION SAVED......\n")
        amount = checkval(currency)
        print(".\n"*3)
        print("OPTION SAVED......\n")
        answer = calc_change(currency,amount)
        print(answer)
        print("Do you wish to continue using the Program ? Press 'y' to continue and 'n' to terminate")
        ans = input()
        while(True):
            if ans not in ['y','n']:
                print("ERROR !!! INVALID ENTRY DETECTED !!! PLEASE TRY AGAIN !!!")
                print(".\n"*3)
                print("Do you wish to continue using the Program ? Press 'y' to continue and 'n' to terminate")
                ans = input()
            else:
                break
   
if __name__ == "__main__":
    main()