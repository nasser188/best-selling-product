products = ["Product A", "Product B", "Product C"]
sales = [1000, 2500, 1500]

counter = 0

for i in range(len(products)):
    counter += 1
    if sales[i] > maxSales:
        maxSales = sales[i]
        bestProduct = products[i]

print("Best-selling product:", bestProduct)

