scores={'network':60,'database':80,'security':50}
key = input('追加する項目名を入力>>')
if key in scores:
    print('すでにとうろくずみおです')
else:
    data=int(input('得点を入力してくだちい>>'))
    scores[key]=data
print(scores)
