import math
#This is a program that can be used to calculate the investments and home loan repayments.
print("investment - to calculate the amount of interest you'll earn on your invest")
print("bond - to calculate the amount you'll have to pay on a home loan")

answer = input("Enter either 'investment' or 'bond' from the menu above investment to proceed: ").lower()

#The use of .lower() will help change any variation of the words 'investment' or 'bond' to lowercase.
#This is an if statement required for the code to recognise 'bond' and 'investment' whether in Upper or Lower case as a valid entry.

if answer == "investment":  
    deposit = float(input("How much money are you depositng? "))
    rate = float(input("Please enter interest rate without symbols: "))
    years = float(input("How many years do you plan on investing? "))
    interest = input("Do you want 'simple' or 'compound' interest? ").lower()
    #Depending on whether the user inputs simple or compound a nested if statement will activate.
    
 
    if interest == "simple":
        print("calculating...")
        rate_divided = float(rate / 100)  
        simple_total = float(deposit * (1 + rate_divided * years))
        print(f"The amound of interest you will earn on your investment is {simple_total:.2f}")

 
    elif interest == "compound":
        print("calculating...")
        rate_divided = float(rate / 100)
        compound_total = float(deposit * math.pow((1 + rate_divided),years))
        print(f"The amount of interest you will earn on your investment is {compound_total:.2f}")

    else:
        print("An error has occured. Please try again.")
        


elif answer == "bond":
        value = float(input("Please enter the present value of the house e.g. 100000 "))
        bond_rate = float(input("Please enter interest rate without symbols: "))
        months = float(input("How many months will it take for you to repay the bond? "))
        print("calculating...")
        b_rate_divided = float((bond_rate / 100) / 12)
        repayment = float((b_rate_divided * value) / (1 - (1 + b_rate_divided ) ** (-months)))
        print(f"The amount you have to repay each is {repayment:.2f}") 


#If the user inputs neither investment, bond or their variations the else sequence will instead occur.
else:
    print("An error has occured. Please try again.")





    

