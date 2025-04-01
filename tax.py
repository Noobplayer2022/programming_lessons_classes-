income = int(input("Enter your income rate: "))

if income < 0:
    rate = 0.00
elif income < 8_925:
    rate = 0.10
elif income < 36_250:
    rate = 0.15
elif income < 87_850:
    rate = 0.23
elif income < 183_250:
    rate = 0.28
elif income < 398_350:
    rate = 0.33
elif income < 400_000:
    rate = 0.35
else:
    rate = 0.396
    

print(f"Your income: ${income:,}")
print(f"Your tax rate is: {rate:.1%}")
