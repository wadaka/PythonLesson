height = float(input('身長(cm)を入力してください>>'))
weight = float(input('体重(kg)を入力してください>>'))
height = height/100
print('あなたのBMI値は「{}」です'.format(weight*(height*height)))
