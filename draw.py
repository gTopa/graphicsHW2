from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    if(x0>x1):
        xTemp=x0
        x0=x1
        x1=xTemp
        yTemp=y0
        y0=y1
        y1=yTemp
    A=y1-y0
    B=-(x1-x0)
    x=x0
    y=y0
    if(A<=-B and A>=0 and B<=0): #Octant 1
        d=2*A+B
        while (x<x1):
            plot(screen,color,x,y)
            if (d>0):
                y+=1
                d+=2*B
            x+=1
            d+=2*A
    if(A>=-B and A>=0 and B<=0): #Octant 2
        d=2*B+A
        while (y<y1):
            plot(screen,color,x,y)
            if (d<0):
                x+=1
                d+=2*A
            y+=1
            d+=2*B
    if(A<=B and A<=0 and B<=0): #Octant 7
        d=A-2*B
        while (y>y1):
            plot(screen,color,x,y)
            if (d>0):
                x+=1
                d+=2*A
            y-=1
            d-=2*B
    if(A>=B and A<=0 and B<=0): #Octant 8
        d=2*A-B
        while(x<x1):
            plot(screen, color, x, y)
            if(d<0):
                y-=1
                d-=2*B
            x+=1
            d+=2*A
