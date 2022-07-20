import tkinter as tk
import random

index = 0
timer = 0
turn = 0
tsugi = 0
winner_checker = False
winner = ""

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e):
    global mouse_x,mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

neko = []
check = []
for i in range(333):
    neko.append([0,0,0])
    check.append([0,0,0])

def draw_neko():
    cvs.delete("NEKO")
    for y in range(3):
        for x in range(3):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60,y*72+60,image=img_neko[neko[y][x]],tag="NEKO")

def check_neko():
    for y in range(3):
        for x in range(3):
            check[y][x] = neko[y][x]

    for y in range(1,2):
        for x in range(2):
            if check[y][x] > 0:
                if check[y-1][x] == check[y][x] and check[y+1][x] == check[y][x]:
                    neko[y-1][x] = 7 
                    neko[y][x] = 7 
                    neko[y+1][x] = 7 

                    return True

    for y in range(3):
        x=1
        if check[y][x] > 0:
            if check[y][x-1] == check[y][x] and check[y][x+1] == check[y][x]:
                neko[y][x-1] = 7
                neko[y][x] = 7
                neko[y][x+1] = 7

                return True

    x=1
    y=1
    if check[y][x] > 0:
        if check[y-1][x-1] == check[y][x] and check[y+1][x+1] == check[y][x]:
            neko[y-1][x-1] = 7
            neko[y][x] = 7
            neko[y+1][x+1] = 7
            return True
        if check[y+1][x-1] == check[y][x] and check[y-1][x+1] == check[y][x]:
            neko[y+1][x-1] = 7
            neko[y][x] = 7
            neko[y-1][x+1]= 7
            return True

    return False

def draw_txt(txt,x,y,siz,col,tg):
    fnt = ("Times New Roman",siz,"bold")
    cvs.create_text(x+2,y+2,text=txt,fill="black",font=fnt, tag=tg)
    cvs.create_text(x,y,text=txt,fill=col,font=fnt,tag=tg)

def game_main():
    global index,timer,turn,tsugi,winner,winner_checker
    global cursor_x,cursor_y,mouse_c
    if index == 0:
        draw_txt("ねこならべ",312,240,100,"violet","TITLE")
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
        draw_txt("げ～むすた～と だにゃ", 312, 420, 40, "white", "TITLE")
        index = 1
        mouse_c = 0
    elif index == 1:
        #初期化処理
        if mouse_c == 1:
            for y in range(3):
                for x in range(3):
                    neko[y][x] = 0
            mouse_c = 0
            turn = 0 
            tsugi = 1 
            winner = ""
            winner_checker = False
            cursor_x = 0
            cursor_y = 0
            draw_neko()
            cvs.delete("TITLE")
            print(str(turn))
            print(str(tsugi))
            print(str(winner))
            print(str(winner_checker))
            print(str(turn))
            index = 2
    elif index == 2:
        if 24 <= mouse_x and mouse_x < 24+72*3 and 24 <= mouse_y and mouse_y < 24+72*3:
            cursor_x = int((mouse_x-24)/72)
            cursor_y = int((mouse_y-24)/72)
            if mouse_c == 1:
                mouse_c = 0
                turn += 1
                neko[cursor_y][cursor_x] = tsugi 
                if turn %2 != 0:
                    tsugi = 2 
                else:
                    tsugi = 1
        index =3 
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x*72+60,cursor_y*72+60,image=cursor,tag="CURSOR")
        draw_neko()
    elif index == 3:
        winner_checker = check_neko()
        draw_neko()
        if winner_checker == True or turn == 9:
            index = 4 
        else:
            index = 2
    elif index == 4:
        timer = timer + 1
        if winner_checker == False:
            winner = "Draw"
        else:
            if turn %2 != 0:
                winner = "1P WIN!"
            else:
                winner = "2P WIN!"

        if timer == 1:
            draw_txt(winner,312,348,60,"red","OVER")
        if timer == 50:
            cvs.delete("OVER")
            index = 0
    elif index == 5:
        timer = timer +1
        if timer == 1:
            draw_txt("Draw",312,348,60,"red","OVER")

    root.after(100,game_main)

root = tk.Tk()
root.title("コポォッ。ねこタソをならべるし（はぁ、はぁ…♡)")
root.resizable(False,False)
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>",mouse_press)
cvs = tk.Canvas(root, width=912, height=768)
cvs.pack()

bg = tk.PhotoImage(file="neko_bg.png")
cursor = tk.PhotoImage(file="neko_cursor.png")
img_neko = [
        None,
        tk.PhotoImage(file="neko1.png"),
        tk.PhotoImage(file="neko2.png"),
        None,
        None,
        None,
        None,
        tk.PhotoImage(file="neko_niku.png")
]

cvs.create_image(456,384,image=bg)
game_main()
root.mainloop()
