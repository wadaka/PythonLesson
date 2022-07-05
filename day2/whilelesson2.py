scores=[80,30,20,64]
for data in scores:
    if data >=60:
        print('合格')
    else:
        print('不合格')

ages=[25,38,7,20,12,49,57,45,4,89,21,5,28,23,58,30,42]
num = 5
samples=list()
for age in ages:
    if 20 <= age <= 30:
        samples.append(age)
        if len(samples) == num:
            break
print(samples)

ages=[25,38,7,20,12,49,57,45,4,89,21,5,28,23,58,30,42,'無回答',3]
num = 5
samples=list()
for data in ages:
    #if not isinstance(data,int):
    if not type(data) is int:
        continue
    if data< 20 or data >= 30:
        continue
    samples.append(data)
print(samples)
