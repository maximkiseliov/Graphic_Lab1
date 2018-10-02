root = Tk()

canv = Canvas(root, width=500, height=500)
canv.pack()
x0 = 40
y0 = 240
xm = 480
ym = 20

def coord(x0, y0, xm, ym, fil_color):
    canv.create_line(x0-220, y0, xm+10, y0, fill=fil_color, arrow=LAST)
    canv.create_line(x0, ym-10, x0, 2*y0-ym+10, fill=fil_color, arrow=FIRST)


def figure(f, fm, tm, x0, y0, xm, ym, fil_color):
    xb = x0
    t = 0
    yb = y0 + (ym - y0)*f(t)/fm
    canv.create_line(xb,yb,xb,yb,fill=fil_color)

    for x in range(x0+2, xm, 2):
        t = tm*(x - x0)/(xm - x0)
        y = y0+(ym - y0)*f(t)/fm
        canv.create_line(xb, yb, x, y, fill=fil_color)
        canv.create_oval(xb, yb, xb, yb, width = 0, fill = 'red')

        xb = x
        yb =y
    
#canv.create_oval(300, 300, 310, 310, width = 0, fill = 'red')

coord(x0, y0, xm, ym, 'blue')
figure(math.sin, 1.2, 7, x0, y0, xm, ym, 'black')
root.mainloop()
