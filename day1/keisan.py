a=10
b=5

answer=a+b
print(a,'+',b,'=',answer)

answer=a-b
print(a,'-',b,'=',answer)

answer=a*b
print(a,'*',b,'=',answer)

answer=a/b
print(a,'/',b,'=',answer)

x=-10
if x>0:
    print('正の数、正の喜びを知りやがって！ゆるさんぞ！くきぃっ！！')
    print('正の数どぅえ～す')
else:
    print('正の数ではない、正の喜びを知らない')

score=64

if score >80:
    print('早見優')
elif score >60:
    print('広末涼子')
elif score > 40:
    print('田原可南子')
else:
    print('和田アキ子')
#これでコメントになっちゃう（なっちゃえ～！）

n=0
while n<10:
    print(n)
    n=n+1

print('シュウ ウエムラ')

name = 'むらまつ~むらむら~'
age = 24
height = 153.24
#大工の源さん「ハンドルを左に戻してくれぃっ！」
print('わたすの名前は{}で、年齢は{}、身長は{}でいっ！'.format(name,age,height))
print(f'わたすの名前は{name}で、年齢は{age}、身長は{height}でいっ！')

print(type(age) is str)
print(type(age) is int)
