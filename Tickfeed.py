from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import yfinance as yf
import numpy as np
import pandas as pd
import time
import os
import pathlib

def place_image2():
    jilimg = PhotoImage(file=img_path2)
    label.img = jilimg
    label.configure(image = jilimg)
    home.after(6000, place_image3)

def place_image3():
    lilimg = PhotoImage(file=img_file_name3)
    label.img = lilimg
    label.configure(image = lilimg)
    home.after(6000, place_image4)

def place_image4():
    nilimg = PhotoImage(file=img_file_name4)
    label.img = nilimg
    label.configure(image = nilimg)
    home.after(6000, place_image2)

home = Tk()

vrule = Frame(home, bg="#FFFFFF", height=800, width=4)
vrule.place(x=500,y=0)


home.attributes('-fullscreen', True)
def departer(p):
    p.attributes('-fullscreen', False)
    p.geometry("1920x1080")


def changer(a,b):
    a.deiconify()
    b.withdraw()
    
home.title("Welcome Page")
home.configure(background = "#202124")
case1 = 2
case2 = 2
case3 = 2
case4 = 2

def FAQ11():
    global case1
    global case2
    global case3
    global case4
    case1 +=1
    case2 = 2
    case3 = 2
    case4 = 2
    if (case1 % 2) == 0:
        FAQ2.place(x=640,y=200)
        FAQ3.place(x=640,y=260)
        FAQ4.place(x=640,y=320)
        FAQ1lab.place_forget()
    else:
        FAQ2.place(x=640,y=400)
        FAQ3.place(x=640,y=450)
        FAQ4.place(x=640,y=500)
        FAQ1lab.place(x=640,y=200)
        FAQ2lab.place_forget()
        FAQ3lab.place_forget()
        FAQ4lab.place_forget()

def FAQ22():
    global case2
    global case1
    global case3
    global case4
    case2 +=1
    case1 = 2
    case3 = 2
    case4 = 2
    if (case2 % 2) == 0:
        FAQ3.place(x=640,y=260)
        FAQ4.place(x=640,y=320)
        FAQ2lab.place_forget()
    else:
        FAQ4.place(x=640,y=500)
        FAQ3.place(x=640,y=440)
        FAQ2lab.place(x=640,y=330)
        FAQ2.place(x=640,y=200)
        FAQ1lab.place_forget()
        FAQ3lab.place_forget()
        FAQ4lab.place_forget()


def FAQ33():
    global case2
    global case1
    global case3
    global case4
    case3 +=1
    case1 = 2
    case2 = 2
    case4 = 2
    if (case3 % 2) == 0:
        FAQ2.place(x=640,y=200)
        FAQ3.place(x=640,y=260)
        FAQ4.place(x=640,y=320)
        FAQ3lab.place_forget()
        FAQ2lab.place_forget()
        FAQ1lab.place_forget()
    else:
        FAQ3.place(x=640,y=260)
        FAQ4.place(x=640,y=550)
        FAQ3lab.place(x=640,y=330)
        FAQ2.place(x=640,y=200)
        FAQ1lab.place_forget()
        FAQ2lab.place_forget()
        FAQ4lab.place_forget()

def FAQ44():
    global case2
    global case1
    global case3
    global case4
    case4 +=1
    case1 = 2
    case2 = 2
    case3 = 2
    if (case4 % 2) == 0:
        FAQ2.place(x=640,y=200)
        FAQ3.place(x=640,y=260)
        FAQ4.place(x=640,y=320)
        FAQ3lab.place_forget()
        FAQ2lab.place_forget()
        FAQ1lab.place_forget()
        FAQ4lab.place_forget()
    else:
        FAQ3.place(x=640,y=260)
        FAQ2.place(x=640,y=200)
        FAQ4.place(x=640,y=320)
        FAQ3lab.place_forget()
        FAQ4lab.place(x=640,y= 500)
        FAQ1lab.place_forget()
        FAQ2lab.place_forget()
        
        
assist = Tk()
assist.attributes('-fullscreen', True)
assist.configure(background = "#202124")
lefttitle = Label (assist, text="How it works", font=("Arial Rounded MT Bold", 35), bg = "#202124", fg="#A2DCEE")
lefttitle.place(x=10,y=10)
help1 = Label(assist, text="1.Choose a stock", font=("HP Simplified Hans", 20),bg = "#202124", fg="#ADEEE2")
help1.place(x=20,y=140)
help2 = Label(assist, text="2.Choose the data function of the stock you want", font=("HP Simplified Hans", 20),bg = "#202124", fg="#ADEEE2")
help2.place(x=20,y=180)
help3 = Label(assist, text="3.Choose the time period for which \n you want the data function", font=("HP Simplified Hans", 20),bg = "#202124", fg="#ADEEE2")
help3.place(x=20,y=220)
help4 = Label(assist, text="4.Press Go to get your tick data", font=("HP Simplified Hans", 20),bg = "#202124", fg="#ADEEE2")
help4.place(x=20,y=280)
p2but1 = Button(assist, text="Back", bg="#A2B9EE", command=lambda assist=assist:changer(home,assist),width=18, height=2, font=("HP Simplified Hans",10) )
p2but1.place(x=250,y=600)
p2but2 = Button(assist, text="exit", width=8, height=1,command=lambda assist=assist:departer(assist))
p2but2.place(x=1210,y=690)
vrule2 = Frame(assist, bg="#FFFFFF", height=800, width=4)
vrule2.place(x=610,y=0)
righttitle = Label (assist, text="Frequently Asked Questions", font=("Arial Rounded MT Bold", 35), bg = "#202124", fg="#A2DCEE")
righttitle.place(x=630,y=10)
FAQ1 = Button(assist, text="1.How many stocks can I choose from?", font=("HP Simplified Hans", 20),bg = "#202124", fg="#ADEEE2",
              command=lambda :FAQ11())
FAQ1.place(x=640,y=140)
FAQ1lab = Button(assist, text="We will be starting off with a small number of popular stocks, and \n will later diversify into a wide variety of stocks and cryptocurrencies",
                font=("HP Simplified Hans", 15),bg = "#202124", fg="#ADEEE2")
FAQ2 = Button(assist, text="2.What data functions are available for me to use?", font=("HP Simplified Hans", 20),bg = "#202124", fg="#ADEEE2", command=lambda :FAQ22())
FAQ2.place(x=640,y=200)
FAQ2lab = Label(assist, text="MAX - maximum price in the specified period \n MIN - minimum price in specified period",
                font=("HP Simplified Hans", 15),bg = "#202124", fg="#ADEEE2")
FAQ3 = Button(assist, text="3.How far back can I get stock data?", font=("HP Simplified Hans", 20),bg = "#202124", fg="#ADEEE2", command=lambda :FAQ33())
FAQ3.place(x=640,y=260)
FAQ3lab = Label(assist, text="10 years",
                font=("HP Simplified Hans", 15),bg = "#202124", fg="#ADEEE2")
FAQ4 = Button(assist, text="4.Do I need an internet connection \n to use the application?", font=("HP Simplified Hans", 20),bg = "#202124", fg="#ADEEE2"
              , command=lambda :FAQ44())
FAQ4.place(x=640,y=320)
FAQ4lab = Label(assist, text="Yes",
                font=("HP Simplified Hans", 15),bg = "#202124", fg="#ADEEE2")

assist.withdraw()
case5 = 1
def bringtolight():
    global case5
    case5 +=1
    if (case5 % 2) == 0:
        vrule.configure(bg="#000000")
        home.configure(background = "#FFFFFF")
        func.configure(background = "#FFFFFF")
        assist.configure(background = "#FFFFFF")
        vrule2.configure(bg="#000000")
        vrule3.configure(bg="#000000")
        togdrk.configure(image = togoff)
        help1.configure(bg = "#FFFFFF",fg="#02528C")
        help2.configure(bg = "#FFFFFF",fg="#02528C")
        help3.configure(bg = "#FFFFFF",fg="#02528C")
        help4.configure(bg = "#FFFFFF",fg="#02528C")
        FAQ1.configure(bg = "#FFFFFF",fg="#02528C")
        FAQ2.configure(bg = "#FFFFFF",fg="#02528C")
        FAQ3.configure(bg = "#FFFFFF",fg="#02528C")
        FAQ4.configure(bg = "#FFFFFF",fg="#02528C")
        FAQ1lab.configure(bg = "#FFFFFF",fg="#02528C")
        FAQ2lab.configure(bg = "#FFFFFF",fg="#02528C")
        FAQ3lab.configure(bg = "#FFFFFF",fg="#02528C")
        FAQ4lab.configure(bg = "#FFFFFF",fg="#02528C")
        lefttitle.configure(bg = "#FFFFFF",fg="#02528C")
        righttitle.configure(bg = "#FFFFFF",fg="#02528C")
        lab1.configure(bg = "#FFFFFF")
        but4.configure(bg = "#FFFFFF")
        but3.configure(bg = "#FFFFFF")
        des1.configure(bg = "#FFFFFF",fg="#02528C")
        des2.configure(bg = "#FFFFFF",fg="#02528C")
        des3.configure(bg = "#FFFFFF",fg="#02528C")
        functit.configure(bg = "#FFFFFF",fg="#02528C")
        shotput.configure(bg = "#FFFFFF",fg="#02528C")
        shotput2.configure(bg = "#FFFFFF",fg="#02528C")
        togdrk.configure(bg = "#FFFFFF")
        dmod.configure(bg = "#FFFFFF")
    else:
        vrule.configure(bg="#FFFFFF")
        home.configure(background = "#202124")
        func.configure(background = "#202124")
        assist.configure(background = "#202124")
        vrule2.configure(bg="#FFFFFF")
        vrule3.configure(bg="#FFFFFF")
        togdrk.configure(image = togon)
        help1.configure(bg = "#202124",fg="#A2DCEE")
        help2.configure(bg = "#202124",fg="#A2DCEE")
        help3.configure(bg = "#202124",fg="#A2DCEE")
        help4.configure(bg = "#202124",fg="#A2DCEE")
        FAQ1.configure(bg = "#202124",fg="#A2DCEE")
        FAQ2.configure(bg = "#202124",fg="#A2DCEE")
        FAQ3.configure(bg = "#202124",fg="#A2DCEE")
        FAQ4.configure(bg = "#202124",fg="#A2DCEE")
        FAQ1lab.configure(bg = "#202124",fg="#A2DCEE")
        FAQ2lab.configure(bg = "#202124",fg="#A2DCEE")
        FAQ3lab.configure(bg = "#202124",fg="#A2DCEE")
        FAQ4lab.configure(bg = "#202124",fg="#A2DCEE")
        lefttitle.configure(bg = "#202124",fg="#A2DCEE")
        righttitle.configure(bg = "#202124")
        lab1.configure(bg = "#202124")
        but4.configure(bg = "#A2B9EE")
        but3.configure(bg = "#A2B9EE")
        des1.configure(bg = "#202124",fg="#A2DCEE")
        des2.configure(bg = "#202124",fg="#A2DCEE")
        des3.configure(bg = "#202124",fg="#A2DCEE")
        functit.configure(bg = "#202124",fg="#A2DCEE")
        shotput.configure(bg = "#202124",fg="#A2DCEE")
        shotput2.configure(bg = "#202124",fg="#A2DCEE")
        dmod.configure(bg = "#202124")
        togdrk.configure(bg = "#202124")
    
        

lab1 = Label(home, text="Tickfeed", font=("Broadway", 75), bg= "#202124", fg= "#7A6EC2")
but1 = Button(home, text="exit", width=8, height=1,command=lambda home=home:departer(home))
but3 = Button(home, text="Help",  font=("HP Simplified Hans",10), width=18, bg="#A2B9EE", height=2,
                 borderwidth = 6, command=lambda home=home:changer(assist,home))
but4 = Button(home, text="Start",  font=("HP Simplified Hans",10), width=18, bg="#A2B9EE", height=2,
                 borderwidth = 6, command=lambda home=home:changer(func,home))
dmod = Label(home, text="Toggle light/dark mode", font=("HP Simplified Hans",10), bg= "#202124", fg="#A2DCEE")
dmod.place(x=1000,y=10)
togon = PhotoImage(file="C:\\Users\\tobzz\\Documents\\TIckfeed\\Pic11.png")
togoff = PhotoImage(file="C:\\Users\\tobzz\\Documents\\TIckfeed\\Picture22.png")
togdrk = Button(home, image = togon, command=lambda home=home:bringtolight(), borderwidth=0, bg = "#202124" )
togdrk.place(x=1150,y=5)
but4.place(x=176, y=400)
but3.place(x=176, y=500)



lab1.place(x=14,y=8)
but1.place(x=1210,y=690)



img_file_name = "Stock44.png"
current_dir = pathlib.Path(__file__).parent.resolve()
img_path = os.path.join(current_dir, img_file_name) 
menu1 = PhotoImage(file=img_path)
label = Label(home, image = menu1, borderwidth=2)
label.place(x=602,y=180)

img_file_name2 = "Stock11.png"
current_dir = pathlib.Path(__file__).parent.resolve()
img_path2 = os.path.join(current_dir, img_file_name2)

img_file_name3 = "Stock33.png"
current_dir = pathlib.Path(__file__).parent.resolve()
img_path3 = os.path.join(current_dir, img_file_name3) 

img_file_name4 = "Stock11.png"
current_dir = pathlib.Path(__file__).parent.resolve()
img_path4 = os.path.join(current_dir, img_file_name4) 

home.after(6000, place_image2)
home.deiconify()

func = Tk()
func.title("Main Menu")
func.attributes('-fullscreen', True)
func.configure(background = "#202124")
vrule3 = Frame(func, bg="#FFFFFF", height=800, width=4)
vrule3.place(x=610,y=0)
functit = Label(func, text="Select your stock, function and Time Period", font=("Arial Rounded MT Bold", 20), bg = "#202124", fg="#A2DCEE")
functit.place(x=10,y=10)
bac3 = Button(func, text="Back", bg="#A2B9EE", command=lambda assist=assist:changer(home,func),width=18, height=2, font=("HP Simplified Hans",10) )
bac3.place(x=250,y=600)
exit3 = Button(func, text="exit", width=8, height=1,command=lambda home=home:departer(func))
exit3.place(x=1210,y=690)

def comget():
    global z
    global high
    global JP
    global low
    JP = yf.Ticker("JPM")
    CS = yf.Ticker("CS")
    GS = yf.Ticker("GS")
    BK = yf.Ticker("BLK")
    MS = yf.Ticker("MS")
    GL = yf.Ticker("GOOGL")
    c = JP.history(period="MAX")
    d = CS.history(period="MAX")
    e = GS.history(period="MAX")
    f = BK.history(period="MAX")
    g = MS.history(period="MAX")
    h = GL.history(period="MAX")
    high = 0
    low = 1000000000000
    choice = drops.get()
    choice2 = str(drops2.get())
    choice3 = int(drops3.get())
    shotput.place_forget()
    shotput2.place_forget()
    func.update()
    if choice == "JPMorgan":
        if choice2 == "MAX":
            i = 1
            while i <= choice3:
                if c.iat[-i,1] > high:
                    high = c.iat[-i,1]
                i = i + 1
            #high = float(high)
            high = round(high,3)
            high = str(high)
            shotput.configure(text = "$" + high)
            #shotput2.place_forget()
            shotput.place(x=800,y=300)
            func.update()
        elif choice2 == "MIN":
            i = 1
            while i <= choice3:
                if c.iat[-i,2] < low:
                    low = c.iat[-i,2]
                i = i + 1
            #low = float(low)
            low = round(low,3)
            low = str(low)
            shotput2.configure(text = "$" + low)
            #shotput.place_forget()
            shotput2.place(x=800,y=300)
            func.update()
    elif choice == "Credit Suisse":
        if choice2 == "MAX":
            i = 1
            while i <= choice3:
                if d.iat[-i,1] > high:
                    high = d.iat[-i,1]
                i = i + 1
            #high = float(high)
            high = round(high,3)
            high = str(high)
            shotput.configure(text = "$" + high)
            #shotput2.place_forget()
            shotput.place(x=800,y=300)
            func.update()
        elif choice2 == "MIN":
            i = 1
            while i <= choice3:
                if d.iat[-i,2] < low:
                    low = d.iat[-i,2]
                i = i + 1
            #low = float(low)
            low = round(low,3)
            low = str(low)
            shotput2.configure(text = "$" + low)
            #shotput.place_forget()
            shotput2.place(x=800,y=300)
            func.update()
    elif choice == "Goldman Sachs":
        if choice2 == "MAX":
            i = 1
            while i <= choice3:
                if e.iat[-i,1] > high:
                    high = e.iat[-i,1]
                i = i + 1
            #high = float(high)
            high = round(high,3)
            high = str(high)
            shotput.configure(text = "$" + high)
            #shotput2.place_forget()
            shotput.place(x=800,y=300)
            func.update()
        elif choice2 == "MIN":
            i = 1
            while i <= choice3:
                if e.iat[-i,2] < low:
                    low = e.iat[-i,2]
                i = i + 1
            #low = float(low)
            low = round(low,3)
            low = str(low)
            shotput2.configure(text = "$" + low)
            #shotput.place_forget()
            shotput2.place(x=800,y=300)
            func.update()
    elif choice == "Blackrock":
        if choice2 == "MAX":
            i = 1
            while i <= choice3:
                if f.iat[-i,1] > high:
                    high = f.iat[-i,1]
                i = i + 1
            #high = float(high)
            high = round(high,3)
            high = str(high)
            shotput.configure(text = "$" + high)
            #shotput2.place_forget()
            shotput.place(x=800,y=300)
            func.update()
        elif choice2 == "MIN":
            i = 1
            while i <= choice3:
                if f.iat[-i,2] < low:
                    low = f.iat[-i,2]
                i = i + 1
            #low = float(low)
            low = round(low,3)
            low = str(low)
            shotput2.configure(text = "$" + low)
            #shotput.place_forget()
            shotput2.place(x=800,y=300)
            func.update()
    elif choice == "Morgan Stanley":
        if choice2 == "MAX":
            i = 1
            while i <= choice3:
                if g.iat[-i,1] > high:
                    high = g.iat[-i,1]
                i = i + 1
            #high = float(high)
            high = round(high,3)
            high = str(high)
            shotput.configure(text = "$" + high)
            #shotput2.place_forget()
            shotput.place(x=800,y=300)
            func.update()
        elif choice2 == "MIN":
            i = 1
            while i <= choice3:
                if g.iat[-i,2] < low:
                    low = g.iat[-i,2]
                i = i + 1
            #low = float(low)
            low = round(low,3)
            low = str(low)
            shotput2.configure(text = "$" + low)
            #shotput.place_forget()
            shotput2.place(x=800,y=300)
            func.update()
    elif choice == "Alphabet":
        if choice2 == "MAX":
            i = 1
            while i <= choice3:
                if h.iat[-i,1] > high:
                    high = h.iat[-i,1]
                i = i + 1
            #high = float(high)
            high = round(high,3)
            high = str(high)
            shotput.configure(text = "$" + high)
            #shotput2.place_forget()
            shotput.place(x=800,y=300)
            func.update()
        elif choice2 == "MIN":
            i = 1
            while i <= choice3:
                if h.iat[-i,2] < low:
                    low = h.iat[-i,2]
                i = i + 1
            #low = float(low)
            low = round(low,3)
            low = str(low)
            shotput2.configure(text = "$" + low)
            #shotput.place_forget()
            shotput2.place(x=800,y=300)
            func.update()

shotput = Label(func, font=("Arial Rounded MT Bold", 30), bg = "#202124", fg="#A2DCEE",width=10,)
shotput2 = Label(func, font=("Arial Rounded MT Bold", 30), bg = "#202124", fg="#A2DCEE",width=10)
fontify = ("HP Simplified Hans", 16)
drops = ttk.Combobox(func, values=["Pick a Stock","Credit Suisse","JPMorgan","Goldman Sachs","Blackrock","Alphabet","Morgan Stanley"],  font = fontify)
drops.current(0)
drops.place(x=320,y=150)
func.option_add('*TCombobox*Listbox.font', fontify)
func.withdraw()
drops2 = ttk.Combobox(func, values=["Pick a function","MAX","MIN"],  font = fontify)
drops2.current(0)
drops2.place(x=320,y=215)

drops3 = Entry(func, width = 20, bg="#DDDCDC",font=("HP Simplified Hans", 14))
drops3.place(x=340,y=270)
#print(drops3.configure())
hetter = Button(func, text="Enter", font=("HP Simplified Hans",10), width=18, bg="#A2B9EE", height=2,
                 borderwidth = 6, command=lambda func=func: comget())
des1 = Label(func, text="Pick a stock", font=("HP Simplified Hans", 14),bg = "#202124", fg="#ADEEE2")
des2 = Label(func, text="Pick a function", font=("HP Simplified Hans", 14),bg = "#202124", fg="#ADEEE2")
des3 = Label(func, text="Enter a time period in days", font=("HP Simplified Hans", 14),bg = "#202124", fg="#ADEEE2")
des1.place(x=100,y=150)
des2.place(x=100,y=210)
des3.place(x=100,y=270)
hetter.place(x=250,y=450)

