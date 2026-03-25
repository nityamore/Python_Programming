def CheckEven(No):
    if(No % 2 == 0):
        print("It is even number")
    else:
        print("It is odd number")


def main():
    value = 0

    print("Enter number :")
    value = int(input())

    CheckEven(value)

main()

