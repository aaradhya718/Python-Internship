balance = 5000
pin = 1234 

user_pin = int(input("Enter your pin"))

if user_pin == pin:
    print("Your balance is:", balance)
    amount = int(input("Enter amount to Withdraw:"))
    balance -= amount  #balance - amount
    print("Congrats amoount withdrawn successfully", "Remaining Balance = ", balance)
else:
    print("Pin incorrect")