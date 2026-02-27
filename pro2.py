# QUE-2 : A tip calculator

print("WELCOME TO THE TIP CALCULATOR")
bill=int(input("what is your total bill?"))
tip=float(input("how many tip would you like to give? 10 20 30:"))
people=int(input("how many people split the bill?"))
bill_with_tip=tip / 100 * bill + bill
bill_per_person=bill/people
final_amt=round(bill_per_person,0)
print(f"each person should pay :{final_amt}")
print=round(final_amt)

