tea_prices = {
    "Masala Tea": 40,
    "Green Tea": 50,
    "Lemon Tea": 80
}
print(tea_prices.items())

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices.items()}
print(tea_prices_usd)