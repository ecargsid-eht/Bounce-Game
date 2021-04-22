from tkinter import *
import random,time

root=Tk()
root.title("Bounce Game")
root.resizable(0,0)     ## Disables the size change

root.wm_attributes("-topmost",1)        #### THIS TELLS TKINTER TO PLACE THE WINDOW OVER ALL OTHER WINDOWS

canvas=Canvas(root,width=500,height=500,bd=0,highlightthickness=0,bg='green')
canvas.pack()


root.update()


class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle = paddle
        self.id=canvas.create_oval(20,20,45,45,fill=color)
        self.canvas.move(self.id,245,100)       ############ GIVES INITIAL POSITION OF THE BALL
        start=[-3,-2,-1,1,2,3]        
        self.x=random.choice(start)
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()       ####################    GIVES THE HEIGHT OF THE CANVAS WINDOW,i.e., 500 IN THIS CASE ##
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom = True


    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
            else:
                return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)

        if pos[1] <=0:
            self.y = 3

        if pos[3]>=self.canvas_height:
            self.hit_bottom = False

        if pos[0] <=0:
            self.x = 3

        if pos[2] >=self.canvas_width:
            self.x = -3

        if self.hit_paddle(pos) == True:
            start = [-2,-3,-1]
            self.y = random.choice(start)


class Paddle:
    def __init__(self,canvas,colour):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=colour)
        self.canvas.move(self.id,200,300)
        self.x=0
        root.bind("<Left>",self.turn_left)
        root.bind("<Right>",self.turn_right)
        self.canvas_width=self.canvas.winfo_width()

    
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x = 2
        
        if pos[2]>=self.canvas_width:
            self.x = -2
        
    def turn_left(self,event):
        self.x=-3

    def turn_right(self,event):
        self.x=3

paddle=Paddle(canvas,'brown')
ball=Ball(canvas,paddle,'red')


while 1:
    if ball.hit_bottom ==True:
        ball.draw()
        paddle.draw()
    else:
        ball.draw()
        canvas.create_text(245,100,text='Game Over!',font=("Arial",40))
    root.update_idletasks()             #############   THIS UPDATES THE BACKGROUND ######################################  
    root.update()                       #############   UPDATES THE FOREGROUND ,i.e, THE BALL   ##########################
    time.sleep(0.01)





root.mainloop()