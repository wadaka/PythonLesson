import tkinter as tk
def btn_calc():
    price=int(entry_price.get())
    person=int(entry_person.get())
    dnum=price/person
    pay=int(dnum // 100 *100)
    if dnum > pay:
        pay+=100
    payorg=price-pay*(person-1)
    label_ans=tk.Label(root,text=f"一人あたり{pay}({person-1}人)、幹事は{payorg}円です.",font=('メイリオ',10))
    label_ans.place(x=10,y=220)

root = tk.Tk()

canvas=tk.Canvas(root,width=400,height=600,bg='skyblue')
#金額入力欄
label_price=tk.Label(root,text='金額',font=('メイリオ',10),bg='skyblue')
label_price.place(x=10,y=10)
entry_price=tk.Entry(width=20)
entry_price.place(x=10,y=50)
#人数入力欄
label_person=tk.Label(root,text='人数',font=('メイリオ',10),bg='skyblue')
label_person.place(x=10,y=100)
entry_person=tk.Entry(width=20)
entry_person.place(x=10,y=150)
#計算ボタン
btn=tk.Button(text='計算する',command=btn_calc)
btn.place(x=10,y=200)

canvas.pack()
root.mainloop()
