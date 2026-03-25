def CheckPerfect(No):

    iSum = 0

    for i in range(1, int((No/2)+1)):
        if(No % i == 0):
            iSum = iSum + i

    return (iSum == No)

    


def main():
    value = 0
    Ret = 0

    print("Enter number :")
    value = int(input())

    Ret = CheckPerfect(value)

    if(Ret == True):
        print(f"{value} is perfect number")
    else:
        print(f"{value} is not perfect number")

main()

