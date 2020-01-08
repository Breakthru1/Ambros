import sys
import math

print("Coin weight(Grams) -> Coin wrappers")

def main():
    weight = int(input("What is the weight of the coins?: "))
    paino = weight
    print("penny(1) \nnickel(2) \ndime(3) \nquarter(4)")
    kolikko = int(input("What coin do you weigh?: "))
    if kolikko == 1:
        print("Total amount of penny wrappers: ", round(paino/2.500)/50)
        print("Total amount of coins: ", round(paino/2.500))
        print("Total estimated value: ", round(paino/2.500)*0.01,"$")
    elif kolikko == 2:
        print("Total amount of nickel wrappers: ", round(paino/5.000)/40)
        print("Total amount of coins: ", round(paino/5.000))
        print("Total estimated value: ", round(paino/5.000)*0.05,"$")
    elif kolikko == 3:
        print("Total amount of dime wrappers: ", round(paino/2.268)/50)
        print("Total amount of coins: ", round(paino/2.268))
        print("Total estimated value: ", round(paino/2.268)*0.10,"$")
    elif kolikko == 4:
        print("Total amount of quarter wrappers: ", round(paino/5.670)/40)
        print("Total amount of coins: ", round(paino/5.670))
        print("Total estimated value: ", round(paino/5.670)*0.25,"$")
    else:
        print("No work")
        sys.exit(0)
        

        

if __name__ == "__main__":
    main()

        
        
    
        
    
    



