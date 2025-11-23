# Taking information from the user
name = input("Enter your name : ") 
age =  int(input("Enter your age : "))
gender = input("Enter your gender : ")
address = input("Enter your address : ")
mobile = int(input("Enter your mobile number : "))
while(mobile// (10**10)<1 or mobile// (10**10)>10):
    print ("Invalid number")
    mobile = int(input("Enter your mobile number : "))
     
choise = int(input("Enter 1 for Savings Account , 2 for Recurring Deposit Account , 3 for FD Account and 4 for loans : "))

if ( choise == 1 ) :
    # Savings Account
    p = float(input("Enter the principal amount : "))
    t = float(input("Enter the time period : "))
    r = 4
    i = 1
    while t >= (i) :
        tran =input("Transactions made in the or not : YES or NO\n" )
        tran.lower()
        if (tran == 'yes') :
            val = int(input("Enter the net value of the transactions : "))
            str = input("Principal amount increased or decreased : ")
            str.lower()
            if (str in ['i' , 'increase']) :
                p = p + val 
            if (str in ['d' , 'decrease']) :
                p = p - val
        I = p*r*t/100  # Calculating the interest
        i += 1
    finalamt = p + I
    print("Name : " , name)
    print("Age : " , age)
    print("Gender : " , gender)
    print("Mobile No. : " , mobile)
    print("Address : " , address)
    print ("The interest earned is : " , I)
    print ("The final amount is : " ,finalamt)

if ( choise == 2 ) :
    # Recurring Deposit Account
    p = float(input("Enter the principal amount : "))
    t = float(input("Enter the time period : "))
    p = float(input("Enter the principal ammount : "))
    t = float(input("Enter the time period : "))
    if (p < 0 or t < 0) :
        print("Invalid input")
    elif (p<=50000):
        r = 4
    elif (p<= 100000 and p>50000):
        r = 4.5
    elif (p<=500000 and p>100000):
        r = 5
    elif (p<=1000000 and p>500000):
        r = 6
    else :
        r = 7
    CI = (p * (1 + r/100)**(t)) - p    # Calculating the interest
    famt = "%.2f" %(p + CI)     # calculating the final amount upto 2 decimal places
    print("Name : " , name)
    print("Age : " , age)
    print("Gender : " , gender)
    print("Mobile No. : " , mobile)
    print("Address : " , address)
    print("The Compound Interest accomulated is : " , CI)
    print("Final amount is : ",famt)

if ( choise == 3 ) :
    # FD Account
    p = float(input("Enter the principal amount : "))
    t = float(input("Enter the time period : "))
    if (p < 0 or t < 0) :
        print("Invalid input")
    elif (p<=50000):
        if ( age < 60 ) :
            r = 4.5
        else : 
            r = 5
    elif (p<= 100000 and p>50000):
        if ( age < 60 ) :
            r = 5
        else :
            r = 5.5
    elif (p<=500000 and p>100000):
        if ( age < 60 ) :
            r = 6
        else :
            r = 7
    elif (p<=1000000 and p>500000):
        if ( age < 60 ) :
            r = 7
        else :
            r = 8
    else :
        if( age < 60 ) :
            r = 8.5
        else :
            r = 9
    SI = (p*r*t)/100      # Calculating the interest
    print("Name : " , name)
    print("Age : " , age)
    print("Gender : " , gender)
    print("Mobile No. : " , mobile)
    print("Address : " , address)
    print("The Simple Interest accomulated is : " , SI)
    famt = p + SI
    print("Final amount is : ",famt)

if ( choise == 4 ) :
    # Loans
    income = int(input("Enter your monthly income : "))
    mortgage = input("Enter what will you keep for mortgage : ")
    amtneed = int(input("Enter the amount you need : "))
    t = int(input("Enter the time period for which the loan is needed : "))
    purpose = ["Property" , "Education" , "Business"]
    choise = int(input(("Enter 1 for property loans , 2 for Education Loans and 3 for Business related loans : ")))
    if (choise == 1) :
        r = 7.5
    elif (choise == 2) :
        r = 4
    elif (choise == 3) :
        r = 6
    else :
        print ("Invalid choise")
    I = (amtneed*r*t)/100        # Calculating the interest
    Totalpay = amtneed + I
    print("Name : " , name)
    print("Age : " , age)
    print("Gender : " , gender)
    print("Mobile No. : " , mobile)
    print("Address : " , address)
    print("Interest to be paid : " , I)
    print("Total amount to be paid after", t, "years is : " ,Totalpay)
    print("Amount to be paid per month : " , Totalpay/(t*12))
    print("Mortgage kept is : " , mortgage)