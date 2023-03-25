# -*- coding: utf-8 -*-
from tkinter import*

root=Tk()
root.title("Fibonacci Series")
root.geometry("600x600")


label_series = Label(root, text="Fibonacci Series")
label_flower = Label(root)
label_spiral = Label(root)

def FibonacciSeries():
    Num = 10
    first_no=0
    second_no=1
    sum=0
    counter=1
    while(counter<=Num):
        label_series["text"] += str(sum) + " "
        counter=counter+1
        first_no=second_no
        second_no=sum
        sum=first_no + second_no
    label_flower["text"]="Flower is Fully Bloomed"
    label_spiral["text"]= "Left Spirals:" + str(first_no) + " Right Spirals :" + str(second_no)
btn=Button(root, text="Click Me", command=FibonacciSeries)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()







root.mainloop()