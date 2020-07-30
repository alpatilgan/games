from tkinter import *
import tkinter.messagebox
import time

window = Tk()
window.title("Bricks")
canvas_width = 600
canvas_height = 500




def new_game():
    canvas = Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()
    puck = canvas.create_oval(170, 170, 180, 180, fill='red')
    paddle = canvas.create_rectangle(260, 470, 340, 480, fill='green')

   

    def you_won():
        canvas.destroy()
        PlayAgain = tkinter.messagebox.askyesno("You Won!!!", "Do you want to play again?")
        if PlayAgain:
            new_game()
        else:
            window.destroy()
            raise SystemExit
        
    def game_over():
        canvas.destroy()
        PlayAgain = tkinter.messagebox.askyesno("Game Over", "Do you want to play again?")
        if PlayAgain:
            new_game()
        else:
            window.destroy()
            raise SystemExit



    def hit_paddle(pos):
        paddle_pos = canvas.coords(paddle)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]: 
                return True
            return False

    def hit_brick(pos):
        for brick in bricks:
            brick_pos = canvas.coords(brick)
            if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
                if pos[3] >= brick_pos[1] and pos[3] <= brick_pos[3]:
                    canvas.delete(brick)
                    bricks.remove(brick)
                    return True
        return False 

    def move_left(evt):
        pos = canvas.coords(paddle)
        if pos[0] > 0:
            canvas.move(paddle, -20, 0)
        
    def move_right(evt):
        pos = canvas.coords(paddle)
        if pos[2] < canvas_width:
            canvas.move(paddle, 20, 0)

    bricks = []

    for i in range(16):
        brick_top = 50
        brick_left = 60+30*i
        brick = canvas.create_rectangle(brick_left, brick_top, brick_left+20, brick_top+20, fill='blue')
        bricks.append(brick)
 
    for i in range(10):
        brick_top = 90
        brick_left = 150+30*i
        brick = canvas.create_rectangle(brick_left, brick_top, brick_left+20, brick_top+20, fill='yellow')
        bricks.append(brick)
    
    for i in range(16):
        brick_top = 130
        brick_left = 60+30*i
        brick = canvas.create_rectangle(brick_left, brick_top, brick_left+20, brick_top+20, fill='orange')
        bricks.append(brick)    
    
    canvas.bind_all('<KeyPress-Left>', move_left)
    canvas.bind_all('<KeyPress-Right>', move_right)

    active = True
    px = 1
    py = 1

    while active:
        canvas.move(puck, px, py)
        pos = canvas.coords(puck)
        if pos[1] <= 0:
            py = 2
        elif pos[3] >= canvas_height:   
            active = False
            game_over()
        if pos[0] <= 0:
            px = 2
        elif pos[2] >= canvas_width:
            px = -2
        
        if hit_paddle(pos):
            py = -2
            
        if hit_brick(pos):
            py = -py
        if (len(bricks) == 0):
            active = False
            you_won()
        
        window.update()
        time.sleep(.015)
    
    
    
    
    
    window.mainloop()

new_game()






























































