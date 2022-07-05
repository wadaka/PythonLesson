import random
while True:
    user=int(input('手をにゅ～りょく[0:グー,1:チョキ,2:パー]>>'))
    pc=random.randint(0,2)
    hands=['グー','チョキ','パー']
    print(f'あなたは{hands[user]}、pcは{hands[pc]}を選択')

    if user == pc:
        print('あいこ')
        continue
    elif (user + 3 -pc) %3 == 1:
        print('てめーの負け')
    else:
        print('あなたの勝ち')
    break


