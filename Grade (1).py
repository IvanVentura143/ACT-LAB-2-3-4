while True:
    print("!PASS OR FAIL")
    Grade = int(input("ENTER YOUR SCORE: "))
    
    if Grade < 0 or Grade > 100:
        print("invalid input")
    elif Grade >= 90:
        print("Grade: A")
    elif Grade >= 80:
        print("Grade: B")
    elif Grade >= 70:
        print("Grade: C")
    elif  Grade >= 60:
        print("Grade D")
    else:
        print("Grade: F")
    
    answer = input("do you wish to continue?:")
    if answer == "no":
        print("ok")
        
        break
    
              

    

