import random
count=int(input('100~1000の範囲の偶数をいくつ生成する>>'))
l1 = [ random.randrange(100,1001,2) for _ in range(count)]
l1.sort(reverse=True)
print(f'{count}個生成しました!降順に表示します{l1}')
