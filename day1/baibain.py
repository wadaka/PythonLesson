n=1
minute=0
days=4
day_minuite=days*60*24
while minute < day_minuite:
    n*=2
    minute+=5
    print(minute,'分後',n)
print(n)
