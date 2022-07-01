for i in range(5):
    print(i)
for i in range(1,11):
    print(i,end=' ')
print()
for i in range(1,4):
    for j in range(1,11):
        print(i*j,end=' ')
    print()

height=int(input('何段のきゃいどぅんをつくりゅ？>>'))
for i in range(height):
    for j in range(i+1):
        print('*',end='')
    print()
