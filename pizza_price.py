# Data List
pizza_list = [{'size':8,"price":10},{'size':10,"price":13},{'size':12,"price":16}]

# Find Mean(X)
total_size = sum([value['size'] for value in pizza_list ])
mean_x = total_size / len(pizza_list)

# Find Mean(Y)
total_price = sum([value['price'] for value in pizza_list ])
mean_y = total_price / len(pizza_list)

# Find Deviation(X)
deviation_x = [value['size'] - mean_x  for value in pizza_list]


# Find Deviation(Y)
deviation_y = [value['price'] - mean_y  for value in pizza_list]

# Find Product Deviation
product_deviation = [x * y for x, y in zip(deviation_x,deviation_y)]

# Find Sum Product Deviation
sum_product_deviation = sum(product_deviation)

# Find square of Deviation x
square_deviation_x = [abs(2 * x) for x in deviation_x]

# Equation LinearRegression y = mx+b

# Find m Value
m_value = sum_product_deviation / sum(square_deviation_x)

# Find b Value
b_value = mean_y - (m_value * mean_x)

size = input("Could you tell me what size pizza you would like? ")

price  = (float(m_value) * float(size)) + b_value

print(f"The cost of a {size}-size pizza is ${max(0,price)}.")