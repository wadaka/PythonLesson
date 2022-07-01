import random

num = random.randint(1,100)
left = 5
print('1~100の数字の中から一つ選んだよ。')
print('そのかすを',left,'回以内にあってね。')
for i in range(1,left+1):
    print(i,'回目、いくつかな？')
    input_num = int(input())
    if num == input_num:
        print('当たり')
        break
    elif i==left:
        pass
    elif num > input_num:
        print('もっと上だよ')
    else:
        print('もっと下だよ')
else:
    print('当たりは',num,'でした。')
