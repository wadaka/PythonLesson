members=['工藤','ぴよん','まいっく']
print(members[0])

members.append('だとう')
members.append('あんだ～そん')
members.append('みすた')
print(members)

members.remove('あんだ～そん')
print(members)

del members[2]
print(members)
a=[10,20,30,40,50]
b=a[1:3]
print(b)#[20,30]
c=a[2:]
print(c)#[20,30]
d=a[:3]
print(d)#[20,30]
e=a[:]
print(e)#[20,30]

print(a[-1])#最後尾を指定

f=a[-2:]#[40,50]
print(f)
q=a[::-1]#[50,40,30,20,10]
print(q)

scores=[95,30,21,1]

total=sum(scores)
print(f'合計{total}')

print(len(scores))#3

"""
sum=30
print(sum)
total=sum(scores)
print(f'合計{total}')
"""
