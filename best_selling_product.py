products = ["Product A", "Product B", "Product C"]
sales = [1000, 2500, 1500]

maxSales = 0
bestProduct = ""

for i in range(len(products)):
    if sales[i] > maxSales:
        maxSales = sales[i]
        bestProduct = products[i]

print("Best-selling product:", bestProduct)
