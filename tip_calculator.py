print("Welcome to the tip calculator.")

Total_bill=float(input("What was the total bill? Rs: "))

Tip_Percent = int(input("What percentage tip would you like to give? 10, 12 or 15? : "))

Total_person = int(input("How many people to split the bill? : "))

percentage_calculate = float(Tip_Percent/100) 

print(percentage_calculate)

Total_amount = Total_bill * percentage_calculate

print(Total_amount)

Total_value = Total_amount + Total_bill

split_value = Total_value/Total_person

print(split_value)

print(f"Each person should pay: Rs{split_value}")