def calc_raw_profit(buy_price, sell_price, units):
    Profit = (sell_price-buy_price)*units
    return Profit
def apply_tax(my_profit):
    Profity=my_profit*0.05
    return Profity

# 1. Calculate the profit and catch it in a variable
my_profit = calc_raw_profit(900, 500, 100)

# 2. Take that "caught" variable and give it to the tax function
my_tax = apply_tax(my_profit)

# 3. Finally, see your actual take-home money
final_amount = my_profit - my_tax
print(f"Total Profit after Tax: Rs. {final_amount}")