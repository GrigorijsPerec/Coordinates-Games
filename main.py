from tkinter import *


# ==================== FUNCTIONS ====================

def Debug():
    #    if action == 1:
    myPos1.config(bg="black")
    myPos2.config(bg="black")
    myPos3.config(bg="black")
    myPos4.config(bg="black")


#    else:
#        myPos1.config(bg="white")
#        myPos2.config(bg="white")
#       myPos3.config(bg="white")
#        myPos4.config(bg="white")

def Reset():
    points.clear()
    b.destroy()

    mb = Tk()
    mb.title("Rules")
    mb.geometry("450x350")
    Rule1 = Label(mb, text="Правило №1: Первая точка поиска должна ставится в левом верхнем углу")
    Rule1.place(x=1, y=1)
    Rule2 = Label(mb, text="Правило №2: Вторая точка поиска должна ставится в правом нижнем углу")
    Rule2.place(x=1, y=30)
    Rule3 = Label(mb, text="Правило №3:")
    Rule3.place(x=1, y=60)
    Rule4 = Label(mb, text="Правило №4:")
    Rule4.place(x=1, y=90)
    mb.mainloop()


def Check():
    if points[2] > myPos1X > points[0] and points[3] > myPos1Y > points[1]:
        print('Point 1: Coordinates determined')
    if points[2] > myPos2X > points[0] and points[3] > myPos2Y > points[1]:
        print('Point 2: Coordinates determined')
    if points[2] > myPos3X > points[0] and points[3] > myPos3Y > points[1]:
        print('Point 3: Coordinates determined')
    if points[2] > myPos4X > points[0] and points[3] > myPos4Y > points[1]:
        print('Point 4: Coordinates determined')
    print("\n ------------------------------- \n")
    Debug()


def drawRect(event):
    global points, b
    points.append(event.x)
    points.append(event.y)
    if len(points) == 4:
        b = Button(root, bg="#a0a8f1", relief=FLAT)
        b.place(x=min(points[0], points[2]),
                y=min(points[1], points[3]))
        b.place(width=(points[2] - points[0]),
                height=(points[3] - points[1]))
        Check()


root = Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)
points = []  # [x1, y1,  x2, y2]

myPos1X = 376
myPos1Y = 23
myPos1 = Frame(root, bg="white")
myPos1.place(x=myPos1X, y=myPos1Y, width=5, height=5)

myPos2X = 208
myPos2Y = 104
myPos2 = Frame(root, bg="white")
myPos2.place(x=myPos2X, y=myPos2Y, width=5, height=5)

myPos3X = 76
myPos3Y = 97
myPos3 = Frame(root, bg="white")
myPos3.place(x=myPos3X, y=myPos3Y, width=5, height=5)

myPos4X = 330
myPos4Y = 353
myPos4 = Frame(root, bg="white")
myPos4.place(x=myPos4X, y=myPos4Y, width=5, height=5)

root.bind("<Button>", drawRect)

db = Tk()
db.geometry('150x70')
db.resizable(width=False, height=False)

Button(db, text='Debug', font=('Arial', 12), command=Debug).pack(side=TOP)
Button(db, text='Reset', font=('Arial', 12), command=Reset).pack(side=TOP)

db.mainloop()
root.mainloop()
