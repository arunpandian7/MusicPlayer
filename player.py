from vlc import MediaPlayer
from tkinter import  *
from tkinter import filedialog
from os import listdir
from os.path import  join


playing=False
first_time=True
window=Tk()

index=0
onlyfiles=[""]
song_name=StringVar()
song_name.set('Choose a folder')

def browser():
    global file_dir
    global onlyfiles
    global player
    onlyfiles=[""]
    file_dir=filedialog.askdirectory()
    player.stop()
    onlyfiles = [f for f in listdir(file_dir) if f.endswith('.mp3')]
    start()
player=MediaPlayer(onlyfiles[index])
def start():
    global index
    global player
    global song_name
    global playing
    global first_time
    song_name.set(onlyfiles[index][:-4])
    player=MediaPlayer(join(file_dir,onlyfiles[index]))
    player.play()
    playing=True
    first_time=False
def player_play():
    global index
    global player
    global song_name
    global playing
    global first_time

    if(first_time):
        first_time=False
        start()
    elif(playing):
        playing=False
        swap_icon(playing)
        player.pause()
    else:
        playing=True
        swap_icon(playing)
        player.play()
def next():
    global index
    global player
    player.stop()
    index+=1
    start()
def prev():
    global index
    global player
    player.stop()
    index-=1
    start()
def swap_icon(temp):
    global varPh
    global pausePh
    global playPh
    if (temp):
        varPh = pausePh
        button2.configure(image=varPh)
        button2.image = varPh
    else:
        varPh = playPh
        button2.configure(image=varPh)
        button2.image = varPh
window.title("MP3 Player")
window.configure(background="black")
window.geometry("300x200")

topFrame=Frame(window)
topFrame.pack(side=TOP)
bottomFrame=Frame(window)
bottomFrame.pack(side=BOTTOM)
#Top Music Informations
label=Label(topFrame,textvariable=song_name,fg='grey',bg='black',font='Roboto')
label.configure(font=('Roboto','24'),width=300)
label.pack()
browse_button=Button(topFrame,text='Browse',font='Roboto',fg='#2ECC71',bg='black',command=browser)
browse_button.pack(fill=X)


#Media Button layout and design
playPh = PhotoImage(file='C:\\Users\\JAYATV\\PycharmProjects\\MusicPlayer\\Images\\play.png')
nextPh = PhotoImage(file='C:\\Users\\JAYATV\\PycharmProjects\\MusicPlayer\\Images\\next.png')
prevPh = PhotoImage(file='C:\\Users\\JAYATV\\PycharmProjects\\MusicPlayer\\Images\\previous.png')
pausePh= PhotoImage(file='C:\\Users\\JAYATV\\PycharmProjects\\MusicPlayer\\Images\\pause.png')

varPh=PhotoImage()


button1=Button(bottomFrame,image=prevPh,bg='black',height=40,width=40,command=prev)
button2=Button(bottomFrame,image=varPh,bg='black',height=40,width=40,command=player_play)
button3=Button(bottomFrame,image=nextPh,bg='black',height=40,width=40,command=next)
button1.image=prevPh
button2.image=varPh
button3.image=nextPh


button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)



window.mainloop()
