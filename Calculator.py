x=input("This is a calculator.\nWhat operation would you like to do?\nIf it is addition, enter 'a'. If it subtraction,\nenter 's'. If it is multpilication, enter 'm'.\nIf it is division, enter 'd': ")

if x not in ['a','s','m','d']:
    print("Must enter in one of 'a', 's', 'm', or 'd'.")

else:
    if x=='a':
        y=(input("Which two numbers would like to add?: "))
        list=y.split(",")
        nums=[]
        for i in list:
            nums.append(int(i))
        n=nums[0]
        m=nums[1]
        print(n+m)

    if x=='s':
        y=(input("Which two number would you like to subtract? The second number you enter will be subtracted from the first one: "))
        list=y.split(",")
        nums=[]
        for i in list:
            nums.append(int(i))
        n=nums[0]
        m=nums[1]
        print(n-m)

    if x == 'm':
        y = (input("Which two numbers would like to multiply?: "))
        list = y.split(",")
        nums = []
        for i in list:
            nums.append(int(i))
        n = nums[0]
        m = nums[1]
        print(n*m)

    if x == 'd':
        y = (input("Which two numbers would like to divide? The first number you enter will be the numerator and the second will be the denominator: "))
        list = y.split(",")
        nums = []
        for i in list:
            nums.append(int(i))
        n = nums[0]
        m = nums[1]
        try:
            print(n/m)
        except Exception as e:
            print("Cannot divide by 0.")

    print("Way to go!")