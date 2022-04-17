print("List sorting program")

while True:

 number1 = input("type the first number:")
 number2 = input("type the second number:")
 number3 = input("type the third number:")
 number4 = input("type the fourth number:")
 number5 = input("type the fifth number:")

 nums = [number1, number2, number3, number4, number5]

 sorting = input("How do you wanna sort this list? Ascending, Descending or none? ")


 if sorting.lower() == ("ascending"):
     AscList = sorted(nums)
     print(AscList)
 
 elif sorting.lower() == ("descending"):
     DesList = sorted(nums, reverse = True)
     print(DesList)
     
 elif sorting.lower() == ("none"):
     print(nums)
 
 else:
    print('invalid choice')
     
 NewList = input("Would you like to sort a new list? Y/N ")
 if NewList in ("Y", "N"):
   if NewList.upper() == ("N"):
    break