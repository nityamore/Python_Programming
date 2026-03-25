def DisplayDigits(No):

    Digit = 0

    while(No != 0):
        Digit = No % 10
        print(Digit)
        No = No / 10

def main():
    value = 0
    
    print("Enter number :")
    value = int(input())

    DisplayDigits(value)
    

main()

