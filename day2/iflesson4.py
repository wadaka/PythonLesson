print('すべての質問にy か n で答えてください')
okane_aruka = input('お金に余裕はありますか？>>')
if okane_aruka:
    onaka_suiteruka=input('おなかがすごく空いてますのん？>>')
    nomitai_kibunka=input('ビールをのみたいれすかぁ～？>>')
    if onaka_suiteruka == 'y' and nomitai_kibunka == 'y':
        print('やっきぬくはいかがぁ～っすきゃ～')
    elif onaka_suiteruka =='y':
        print('きゃるぅえ～ぃはいきゃっぎゃぁっすきゃぁ～～？')
    elif nomitai_kibunka == 'y':
        print('やっきとぅりはいきゃぎゃっすきゃ～？')
    else:
        print('パスタはいかがっすか？（目を閉じっれば億千の星～♪)')
    yashoku_ituka=input('夜食は必要ですか>>')
    if yashoku_ituka == 'y':
        print('そんなに食ってたら、太るぞ')
else:
    print('家で食え')

