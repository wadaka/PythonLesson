height=input('身長(cm)を入力してくだちい>>')
weight=input('たいじゅ～(kg)を入力してくだちい>>')
height=float(height)/100
weight=float(weight)
bmi=weight/(height*height)
print(bmi)
if bmi>=25:
    result='肥満'
elif bmi>=18.5:
    result='標準体系'
else:
    result='ガリガリ'
print(result)
