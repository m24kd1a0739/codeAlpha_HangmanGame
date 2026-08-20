# CodeAlpha Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 180,
    "MSFT": 420
}

print("======================================")
print("       STOCK PORTFOLIO TRACKER")
print("======================================")

total_investment = 0

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = stock_prices[stock]
        investment = price * quantity

        print(f"Stock Price: ${price}")
        print(f"Quantity: {quantity}")
        print(f"Investment: ${investment}")

        total_investment += investment

    except ValueError:
        print("Please enter a valid quantity.")

print("\n======================================")
print(f"TOTAL INVESTMENT: ${total_investment}")
print("======================================")

# Save the result to a text file
with open("portfolio_result.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("=======================\n")
    file.write(f"Total Investment: ${total_investment}\n")

print("Result saved to portfolio_result.txt")
