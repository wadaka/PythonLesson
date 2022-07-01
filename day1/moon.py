dist=384400000000
thickness=1
count=0

while thickness < dist:
    thickness=thickness*2
    count=count+1
    print(count,'回折り曲げた','厚み:',thickness)
