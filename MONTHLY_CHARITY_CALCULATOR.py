print("Hello!\nWelcome to your monthly CHARITY CALCULATOR!")
salary = float(input("How much is your monthly salary"))
amount_to_charity = int(input("How many percent do you want to give to charity? 5, 10, 15, 20"))
beneficiaries = int(input("How many people will benefit from your charity?"))
amount_to_charity_in_percentage = amount_to_charity / 100
total_charity_amount = salary * amount_to_charity_in_percentage
amount_per_beneficiaries = total_charity_amount / beneficiaries
final_amount_to_beneficiaries = round(amount_per_beneficiaries, 2)
print(f"Each beneficiaries should have {final_amount_to_beneficiaries}")
