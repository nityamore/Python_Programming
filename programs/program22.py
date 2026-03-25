def SumDigits(No):

    Digit = 0
    Sum = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10               # // - Floor division

    return Sum

def main():
    value = 0
    Ret = 0
    
    print("Enter number :")
    value = int(input())

    Ret = SumDigits(value)

    print("Sum of digits is :",Ret)
    

main()

