input_sex=input('男か女か、選べ!! >>')
input_age=int(input('年齢は!? >>'))
result = 'false'
if input_sex in '男':
    if input_age >=18:
        result = 'true'
else:
    if input_age >=16:
        result = 'true'

if result in 'true':
    print('結婚可！俺の子を産めっっっ！！')
else:
    print('結婚不可!帰れっっっ！！')

