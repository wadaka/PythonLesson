import random
count = int(input('さいころなんかいでんしゃ？>>'))
dices=[random.randint(1,6) for _ in range(count)]
print(dices)
print(f'出た値は{set(dices)}の{len(set(dices))}種類')
