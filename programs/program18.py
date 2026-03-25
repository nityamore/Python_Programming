def SumFactors(No):

    iSum = 0

    for i in range(1, int((No/2)+1)):
        if(No % i == 0):
            iSum = iSum + i

    return iSum

    


def main():
    value = 0
    Ret = 0

    print("Enter number :")
    value = int(input())

    Ret = SumFactors(value)

    print("Sum of factors :",Ret)

main()

