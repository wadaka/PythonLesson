#エラー1:EOL while scanning string literal
#print('hello)

'''
-------------------------------
# expected an indented block
elseのブロックになにもはいってねえ！
-------------------------------

x=10
if(x<10):
    print('hoge')
else:

'''
'''
--------------------------------
# invalid non-printable character U+3000
xの後ろに、全角の空欄！(なんで、うまくコードが読めん！)
--------------------------------
x　=10
print(x)

'''
'''
--------------------------------
# name 'x' is not defined
xが定義されてねえ！
--------------------------------
print(x)
'''

try:
    price = int(input('料金を入力>>'))
    number = int(input('人数を入力>>'))
    print('一人あたり{}円です'.format(price/number))
except ValueError:
    print('料金または人数は整数を入力してちょ！')
print('プログラムを終了します')
