rate=float(input("What is the current exchange rate for the Euro to Dollar? (EUR to USD):")
)
money_input= float(input("How much Euro for exchange?:"))
USD = money_input * rate
exchange_fee= 3
amount_for_user= USD- exchange_fee
amount_to_exchange = round(amount_for_user)
##print("Amount to exchange: "+ str(amount_to_exchange))
print(f"amount to exchange: {amount_to_exchange}")