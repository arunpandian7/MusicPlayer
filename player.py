import os
import pandas as pd
from tkinter import  *
from tkinter import filedialog
from PIL import Image

def browser():
    global file_dir
    file_dir=filedialog.askdirectory()





window=Tk()
window.title("MP3 Player")
window.configure(background="black")
window.geometry("600x400")

topFrame=Frame(window)
topFrame.pack(side=TOP)
bottomFrame=Frame(window)
bottomFrame.pack(side=BOTTOM)
#Top Music Informations
label=Label(topFrame,text="Lose Yourself - Eminem",fg='grey',bg='black',font='Roboto')
label.pack()
browse_button=Button(topFrame,text='Browse',font='Roboto',fg='grey',bg='black',command=browser)
browse_button.pack()


#Media Button layout and design
playPh = PhotoImage(file='C:\\Users\\JAYATV\\PycharmProjects\\MusicPlayer\\Images\\icons8-play-96.png')
nextPh = PhotoImage(file='C:\\Users\\JAYATV\\PycharmProjects\\MusicPlayer\\Images\\forward.png')
prevPh = PhotoImage(file='C:\\Users\\JAYATV\\PycharmProjects\\MusicPlayer\\Images\\rewind.png')

button1=Button(bottomFrame,image=prevPh,bg='black',height=80,width=80)
button2=Button(bottomFrame,image=playPh,bg='black',height=80,width=80)
button3=Button(bottomFrame,image=nextPh,bg='black',height=80,width=80)
button1.image=prevPh
button2.image=playPh
button3.image=nextPh


button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)



window.mainloop()
