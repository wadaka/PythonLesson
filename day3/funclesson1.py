def hello():
    print('HELLO')

hello()

def hello(name):
    print('こんちゃ、{}です。'.format(name))

hello('ちんぽす')
hello('みなみ')

def profile(name,age,hobby):
    print('私の名前は{}です。'.format(name))
    print('年齢は{}です。'.format(age))
    print('趣味は{}です。'.format(hobby))

profile('ちんぽす','48','菜園')

def plus(x,y):
    answer=x-y
    return answer

answer=plus(150,50)
print(answer)

def plus_and_minus(a,b):
    return a+b,a-b

next,prev=plus_and_minus(1978,1)

print(next)
print(prev)

def eat(breakfast,lunch,dinner='カレー'):
    print('朝は{}を食い申した'.format(breakfast))
    print('昼は{}を食い申した'.format(lunch))
    print('晩は{}を食い申した'.format(dinner))

eat('バナナ','おにぎり')
eat('バナナ','そば','焼酎')

def eat(breakfast,lunch='ラーメソ',dinner='カレー'):
    print('朝は{}を食い申した'.format(breakfast))
    print('昼は{}を食い申した'.format(lunch))
    print('晩は{}を食い申した'.format(dinner))

eat(breakfast='なっとぅ',dinner='うんこかれー')
eat(dinner='うんこかれー',breakfast='なっとうんこ')
eat('うんこ(生)',dinner='うんこかれー')

def eat(breakfast,lunch='ラーメソ',dinner='カレー',desserts=()):
    print('朝は{}を食い申した'.format(breakfast))
    print('昼は{}を食い申した'.format(lunch))
    print('晩は{}を食い申した'.format(dinner))
    for d in desserts:
        print('おやつに{}を食べました。'.format(d))

eat('トースト','ぱすた','かれ～',('うんこ','ちょこ(意味深)'))
def eat(breakfast,lunch='ラーメソ',dinner='カレー',*desserts):
    print('朝は{}を食い申した'.format(breakfast))
    print('昼は{}を食い申した'.format(lunch))
    print('晩は{}を食い申した'.format(dinner))
    for d in desserts:
        print('おやつに{}を食べました。'.format(d))
eat('トースト','ぱすた','かれ～','うんこ','ちょこ(意味深)','まん','ちん','かん')

def eat(**kwargs):
    for key in kwargs:
        print('{}に{}を食べました'.format(key,kwargs[key]))
eat(朝食='なとぅ',おそめのらんち='ぱすた',はやめのでぃなー='あああああ',よる='おんな')
