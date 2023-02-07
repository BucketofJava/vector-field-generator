from tkinter import *
from tkinter import ttk
from math_interp import interpret;

root=Tk()
#frm=ttk.Frame(root, padding=10)
height=740
width=1000
canvas=Canvas(root, bg="gray", height=height, width=width)
grid_size_x=int(width/20)+1
grid_size_y=int(height/20)+1
middle_x=(grid_size_x-1)*10
middle_y=(grid_size_y)*10
func_str_x=input("Input a function for the x component:: ")
func_str_y=input("Input a function for the y component:: ")
x_dist=int(input("What would you like the horizontal distance between each vector to be:: "))
y_dist=int(input("What would you like the horizontal distance between each vector to be:: "))
normalize=int(input("Would you like to normalize the vectors (1 for yes, 0 for no):: "))
x_func=interpret(func_str_x)
y_func=interpret(func_str_y)
for i in range(grid_size_x-1):
    for j in range(grid_size_y-1):
        canvas.create_rectangle(20*i, 20*j, 20*(i+1), 20*(j+1), width=0.25)
        # print(float((i+1)-middle_x/10))
        # print(float(middle_y/10-(j+1)))
        if(i%x_dist==0 and j%y_dist==0):
            x_coordinate=float((20*(i+1)-middle_x)/20)
            y_coordinate=float((middle_y-20*(j+1))/20)
            x_increase=x_func(x_coordinate, y_coordinate)
            y_increase=-y_func(x_coordinate, y_coordinate)
            if(normalize==1):
                norm=(x_increase**2+y_increase**2)**(1/2)
                if(norm != 0):
                    x_increase/=norm;
                    y_increase/=norm;
            # if(i==0 and j<=5):
            #     print(x_coordinate)
            #     print(y_coordinate)
            #     print(x_increase)
            #     print(y_increase)
            canvas.create_line(20*(i+1), 20*(j+1), 20*(i+1)+20*x_increase, 20*(j+1)+20*y_increase, fill="purple", arrow=LAST, smooth=True, width=2)
canvas.create_line(0, middle_y+20, 1000, middle_y+20, width=2, fill="blue")
canvas.create_line(middle_x-20, 0, middle_x-20, 750, width=2, fill="blue")

#canvas.create_rectangle(0, 0, (100), (100), width=0.25)
canvas.pack()

root.mainloop()



