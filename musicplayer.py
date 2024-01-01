from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer 

root= Tk()
root.title("Music Player")
root.geometry('352x255')
root.configure(bg="white")
root.resizable(width=False, height=False)

def play_music():
    running= listbox.get(ACTIVE)
    running_song['text']= running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def continue_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    playing= running_song['text']
    index= songs.index(playing)
    new_index= index +1
    playing= songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)
    show()
    listbox.select_set(new_index)

    running_song['text']= playing

def previous_music():
    playing= running_song['text']
    index= songs.index(playing)
    new_index= index -1
    playing= songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)
    show()
    listbox.select_set(new_index)

    running_song['text']= playing


left_frame= Frame(root, bg="white", width=140, height=180)
left_frame.grid(row=0, column=0)

right_frame= Frame(root,width=150, height=150, bg="deep pink")
right_frame.grid(row=0, column=1)

down_frame= Frame(root, width=500, height=80, bg="grey")
down_frame.grid(row=1, column=0, columnspan=5, padx=0, pady=1)

running_song= Label(down_frame, text="Choose a song", height=1, width=50, anchor=NW)
running_song.place(x=0,y=1)

img1= Image.open("musicicon.jpeg")
img1= img1.resize((120,150))
img1= ImageTk.PhotoImage(img1)
app_image= Label(left_frame,  image= img1, bg="white",padx=10, pady=10)
app_image.place(x=0, y=10)

img2= Image.open("previousbutton.png")
img2= img2.resize((30, 30))
img2= ImageTk.PhotoImage(img2)
prev_image= Button(down_frame, height=30,width=30, image= img2, padx=10,pady=10, command= previous_music)
prev_image.place(x=50+10, y=30)

img3= Image.open("playbutton.jpeg")
img3= img3.resize((30, 30))
img3= ImageTk.PhotoImage(img3)
play_image= Button(down_frame, height=30,width=30, image= img3, padx=10,pady=10, command= play_music)
play_image.place(x=60+40, y=30)

img4= Image.open("pause button.png")
img4= img4.resize((30, 30))
img4= ImageTk.PhotoImage(img4)
pause_image= Button(down_frame, height=30,width=30, image= img4, padx=10,pady=10, command= pause_music)
pause_image.place(x=100+40, y=30)

img5= Image.open("nextbutton.jpg")
img5= img5.resize((30, 30))
img5= ImageTk.PhotoImage(img5)
next_image= Button(down_frame, height=30,width=30, image= img5, padx=10,pady=10, command= next_music)
next_image.place(x=140+40, y=30)

img6= Image.open("continuebutton.png")
img6= img6.resize((30, 30))
img6= ImageTk.PhotoImage(img6)
continue_image= Button(down_frame, height=30,width=30, image= img6, padx=10,pady=10, command= continue_music)
continue_image.place(x=180+40, y=30)

img7= Image.open("stop button.png")
img7= img7.resize((30, 30))
img7= ImageTk.PhotoImage(img7)
stop_image= Button(down_frame, height=30,width=30, image= img7, padx=10,pady=10, command= stop_music)
stop_image.place(x=220+40, y=30)


listbox= Listbox(right_frame, font=("Arial 9 bold"), selectmode=SINGLE, width=22, bg= "deep pink", fg= "white")
listbox.grid(row=0, column=0)

w= Scrollbar(right_frame)
w.grid(row=0, column=1)

listbox.config(yscrollcommand=w.set)
w.config(command= listbox.yview)

os.chdir(r'C:\Users\Harini\Documents\Python\music')
songs= os.listdir()

def show():
    for i in songs:
        listbox.insert(END, i)

show()

mixer.init()
music_state= StringVar()
music_state.set("Choose one!")

root.mainloop()

