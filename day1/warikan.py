price = input('合計料金>>')
number = input('人数>>')
print(type(price))
print(type(number))
price = int(price)
number = int(number)
money = price / number
money = int(money)

"""
型チェッカー---------------
print(type(price))
print(type(number))
print(type(money))

"""
#文字列連結できるのは、str型のみのため、moneyはstr型に変換しないとエラーになる
money = str(money)
print('一人当たりの支払額は'+money+'です')
