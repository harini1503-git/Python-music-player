from tkinter import *
import pygame
import os

root= Tk()
root.title('Music Player')
root.geometry("500x300")

pygame.mixer.init()

songlist = Listbox(root, background="black", foreground="white", width=100, height=15)
songlist.pack()

play_button_image= PhotoImage(file='playbutton.jpeg')
pause_button_image= PhotoImage(file='pausebutton.png')
next_button_image= PhotoImage(file='nextbutton.jpeg')
previous_button_image= PhotoImage(file='previousbutton.png')

control_frame= Frame(root)
control_frame.pack()

play_button= Button(control_frame, image=play_button_image, borderwidth=0)
root.mainloop()