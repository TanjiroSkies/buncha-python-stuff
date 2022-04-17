def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')

print("Binary converter")

num = int(input("Insert the decimal number you want to be converted into binary: "))

decimalToBinary(num)

