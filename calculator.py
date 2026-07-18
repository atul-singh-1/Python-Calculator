while True:
    print("\n======Calculator======")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Power")
    print("7. Exit")
    try:
        choice=int(input("Enter your choice :"))
    except ValueError:
        print(" Bro! Enter a number! Alphabet and symbol won't work here!")
        continue
    if choice==7:
        print("calculator closed")
        break
    if choice < 1 or choice > 7:
        print("Invalid choice! Please enter a number between 1 and 6.")
       
        continue
    try:
        a=float(input("Enter number A :"))
        b=float(input("Enter number B :"))
    except ValueError:
         print("Bro! Enter a number! Alphabet and symbol won't work here!")
         continue
    if choice==1:
        print("Your answer is =",a+b)
    
    elif choice==2:
        print("Your answer is =",a-b)
        
    elif choice==3:
        print("Your answer is =",a*b)

    elif choice==4:
        if b!=0:
            print("Your answer is =",a/b)
        else:
            print("Division by zero is not possible  ")

    elif choice==5:
        if b!=0:
            print("Your answer is =",a%b)
        else:
            print("Modulus of zero is not possible")   
    
    elif choice==6:
        print("Your answer is =",a**b)
    
    else:
        print("invalid choice !")
