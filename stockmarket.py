def calculate_average_price(stock_data, symbol):
 

  total_price = 0.0
  count = 0

  for data_point in stock_data:
    current_symbol, _, current_price = data_point  

    if current_symbol == symbol:
      total_price += current_price
      count += 1

  if count == 0:
    return None

  return total_price / count

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("AAPL", "2021-01-04", 131.0),
    
]

stock_to_analyze = "AAPL"

average_price = calculate_average_price(stock_data, stock_to_analyze)

if average_price is not None:
  print(f"Average closing price of {stock_to_analyze} over all dates: ${average_price:.2f}")
else:
  print(f"No data found for stock symbol {stock_to_analyze}.")