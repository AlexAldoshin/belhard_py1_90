'''
запросить цену закупки телефона и выдать следующую информацию.
	- цена продажи (+30% к цене закупке)
	- цена продажи со скидкой 5%
	- цена продажи со скидкой 10%
	- цена продажи со скидкой 15%
'''

tel_price = float(input("Введите цену закупки телефона: "))
tel_price_prod = tel_price + tel_price * 0.3
tel_price_prod_d5 = tel_price_prod - tel_price_prod * 0.05
tel_price_prod_d10 = tel_price_prod - tel_price_prod * 0.1
tel_price_prod_d15 = tel_price_prod - tel_price_prod * 0.15

print("- цена продажи", tel_price_prod)
print("- цена продажи со скидкой 5%", tel_price_prod_d5)
print("- цена продажи со скидкой 10%", tel_price_prod_d10)
print("- цена продажи со скидкой 15%", tel_price_prod_d15)