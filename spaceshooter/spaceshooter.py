from tkinter import *
import tkinter.messagebox
import time
import random
import winsound
window = Tk()
window.title("Space Shooter")
img1 = PhotoImage(file="ship.png")
img2 = PhotoImage(file="missle_purple.png")
img3 = PhotoImage(file="missle_red.png")
points = 0

def play_shoot():
    winsound.PlaySound("shoot.wav", 1)
    
def play_boom():
    winsound.PlaySound("explosion.wav", 1)
        
def play_launch():
    winsound.PlaySound("launch.wav", 1)
            
def new_game():
    active = True
    global points
    points = 0
    play_launch()
    canvas = Canvas(window, width = 800, height = 650)
    canvas.pack()
    ship = canvas.create_image(360, 550, anchor=NW, image=img1)
    rand_left = random.randint(50,750)
    rand_top = random.randint(100,700)
    missile1 = canvas.create_image(rand_left, -rand_top, anchor=NW, image=img2)
    rand_left = random.randint(50,750)
    rand_top = random.randint(100,700)
    missile2 = canvas.create_image(rand_left, -rand_top, anchor=NW, image=img3)
    score = Label(window, text="Score: 0")
    score.config(font=("Courier", 24))
    score.pack()
    
    def game_over():
        play_boom()
        active = False 
        canvas.destroy()
        score.destroy()
        PlayAgain = tkinter.messagebox. askyesno9("Game Over" , "Do you want to play again?")
        if PlayAgain:
            new_game()
        else:
            window.destroy()
            raise SystemExit
    
    def update_score():
        global points
        score.config(text="Score: %i" % points)
        score.update_idletasks()
        
    shots = []
    
    def shoot(evt):
        pos = canvas.coords(ship)
        shot = canvas.create_oval(pos[0]+35, 530, pos[0]+40, 540, fill='red')
        shots.append(shot)
        play_shoot()
        
        
    def move_shots():
            for shot in shots:
                canvas.move(shot, 0, -5)
                pos = canvas.coords(shot)
                m1_pos = canvas.coords(missile1)
                m2_pos = canvas.coords(missile2)
                if pos[1] <= 0:
                    canvas.delete(shot)
                    shots.remove(shot)
                elif pos[1] <= m1_pos[1]+257 and pos[1] > m1_pos[1]:
                    if pos[0] >= m1_pos[0]+5 and pos[0] <= m1_pos[0]+67:
                        reset_missile1()
                        canvas.delete(shot)
                        shots.remove(shot)
                elif pos[1] <= m2_pos[1]+257 and pos[1] > m2_pos[1]:
                    if pos[0] >= m2_pos[0]+5 and pos[0] <= m2_pos[0]+67:
                        reset_missile2()
                        canvas.delete(shot)
                        shots.remove(shot)
                        
                        
                
                    
            
                    
                
    def move_missiles():
        canvas.move(missile1, 0, 2)
        pos = canvas.coords(missile1)
        ship_pos = canvas.coords(ship)
        if pos[1]+257 >= 650:
            new_game()
        elif pos[1]+257 >= 550 and pos[0]+67 >= ship_pos[0] and pos[0] <= ship_pos[0]+76:
            new_game()
        canvas.move(missile2, 0, 2)
        pos = canvas.coords(missile2)
        ship_pos = canvas.coords(ship)
        if pos[1]+257 >= 650:
            new_game()
        elif pos[1]+257 >= 550 and pos[0]+67 >= ship_pos[0] and pos[0] <= ship_pos[0]+76:
            new_game()
            
    def reset_missile1():
         rand_left = random.randint(50,750)
         rand_top = random.randint(100,700)
         canvas.coords(missile1,rand_left, -rand_top)
         play_boom()
         global points
         points += 10
         update_score()
         
    def reset_missile2():
         rand_left = random.randint(50,750)
         rand_top = random.randint(100,700)
         canvas.coords(missile2,rand_left, -rand_top)
         play_boom()
         global points
         points += 10
         update_score()
         
            
            

            
        
    def move_left(evt):
        pos = canvas.coords(ship)
        if pos[0] > 0:
            canvas.move(ship, -15, 0)
            
    def move_right(evt):
        pos = canvas.coords(ship)
        if pos[0] < 725:
            canvas.move(ship, 15, 0)
            
    canvas.bind_all('<KeyPress-Left', move_left)
    canvas.bind_all('<KeyPress-Right', move_right)
    canvas.bind_all('<space>', shoot)
    
    
    while active:
        move_shots()
        move_missile()
        window.update()
        time.sleep(0.015)
        
    
    
new_game()
    