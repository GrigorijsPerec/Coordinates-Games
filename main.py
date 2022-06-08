from tkinter import *


# ==================== FUNCTIONS ====================

def Debug():
    global dg

    dg = Tk()
    dg.title("Debug")
    dg.geometry("350x200")
    Button(dg, text='Rules', font=('Arial', 12), command=Rules).grid(column=1, row=1)
    dg.mainloop()


def Reset():
    pass


def Rules():
    global mb

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


def drawRect(event):
    global points
    points.append(event.x)
    points.append(event.y)
    if len(points) == 4:
        b = Button(root, bg="white")
        b.place(x=min(points[0], points[2]),
                y=min(points[1], points[3]))
        b.place(width=abs(points[2] - points[0]),
                height=abs(points[3] - points[1]))
        print(points)
        Check()


root = Tk()
root.geometry("500x400")
root.resizable(width=False, height=False)
points = []  # [x1, y1,  x2, y2]

myPos1X = 3
myPos1Y = 3
# Label(root, fg="black", bg="black").place(x=myPos1X, y=myPos1X+1)
myPos2X = 208
myPos2Y = 104
# Label(root, bg="black").place(x=myPos2X, y=myPos2X+1)
myPos3X = 76
myPos3Y = 97
# Label(root, bg="black").place(x=myPos3X, y=myPos3X+1)
myPos4X = 330
myPos4Y = 353
# Label(root, bg="black").place(x=myPos4X, y=myPos4X+1)

root.bind("<Button>", drawRect)
Button(root, text='Debug', font=('Arial', 12), command=Debug).grid(column=0, row=0)

root.mainloop()
