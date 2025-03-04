
file = open("currency.csv", "r")
lines = file.readlines()
file.close()


exchange_rates = {}

for line in lines[1:]:
    data = line.strip().split(",")
    currency = data[0]  
    rate = float(data[2])  
    exchange_rates[currency] = rate


dollars = float(input("How much dollar do you have? "))
currency = input("What currency you want to have? ").upper()


if currency in exchange_rates:
    converted_amount = dollars * exchange_rates[currency]
    print("\nDollar:", dollars, "USD")
    print(currency + ":", converted_amount)
else:
    print("Currency not found in the exchange rates.")
