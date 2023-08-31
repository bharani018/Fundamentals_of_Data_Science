import pandas as pd
data = {
    'products': ['kurkure', 'lays', 'bingo', 'max', 'lays', 'mad angles', 'lays', 'kurkure', 'kurkure', 'lays'],
    'order_quantity': [50, 80, 44, 19, 48, 34, 89, 97, 78, 69]
}
sales = pd.DataFrame(data)

sorting_sales_price = sales.sort_values(by='order_quantity', ascending=False)

top_products = sorting_sales_price.head(5)
print(f"The Top Selling Product of the Past Month are \n {top_products}")
