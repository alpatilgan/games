from tkinter import *
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
    missile1 = canvas.create_image(200, 100, anchor=NW, image=img2)
    missile2 = canvas.create_image(500, 100, anchor=NW, image=img3)
    score = Label(window, text="Score: 0")
    score.config(font=("Courier", 24))
    score.pack()
    
    while active:
        window.update()
        time.sleep(0.15)
    
    
    
    