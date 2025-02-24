print("ali chegini")
i = 0
count = int(input("enter the number of year: "))
while i < count:
    a = int(input("Enter your year: "))
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        print(f"{a} is ok year")
    else:
        print(f"{a} is not ok year")
    i +=1
    print(f"number of year you wanted{count}")
    
    
