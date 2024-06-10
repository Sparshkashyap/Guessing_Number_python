import random


def call():
    print("\n=================[Welcome to Guess the Number]==========================\n")

    print("\n===[you are provide 6 chance to win the game]===\n")
    
    num1=int(input("Enter the lower bound of the number range :"))
    num2=int(input("Enter the upper bound of the number range :"))

    guessing_number=random.randint(num1,num2)

    k=6
    c=1

    for i in range(1,7):
        
        num=int(input("\nEnter the Guessing Number :"))
        print()

        
        if guessing_number==num :
            
            print("\nHurrah! you have won the match\n")
            c=1
            break

            
           
            
        elif(num>guessing_number):
            
            print("\nThe Guessed number is Higher \n")  
            k=k-1
            print(f"\nYou are only {k} chance left \n")
            if k==1:
                print(f"Hint :{guessing_number}")
            else:
                print("Try again")
        
        # elif(k==0):
        #     print("Try again never give up")
            
        
        else:
            
            print("\nThe Guessed number is lower \n")  
            k=k-1
            #print(k)
            print(f"\nYou are only {k} chance left\n") 
            if k==1:
                print(f"Hint :{guessing_number}")
            else:
                print("Try again")
     
    if c==1 or k==0:
        again()
      
        

def again():
    print("[Match is over]") 
    print()  
    print("Do you want to play again :(yes/no)") 
    print()
    num=input("Enter your choice :")
    if num=="yes":
        call()
    else:
        print("\n[Thanku for playing Game]\n")
        return
          


call()




