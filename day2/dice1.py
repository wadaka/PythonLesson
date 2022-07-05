import random
count = int(input('さいころをんなんかいふる？>>'))
dices=[random.randint(1,6) for _ in range(count)]
print(dices)
print(f'合計は{sum(dices)}でした。')
