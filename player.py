from vlc import MediaPlayer
from vlc import libvlc_media_player_get_position as get_pos
from vlc import libvlc_media_player_get_length as get_len
from vlc import libvlc_audio_set_volume,libvlc_audio_get_volume
from vlc import libvlc_media_player_is_playing
from tkinter import  *
from tkinter import filedialog
from tkinter import messagebox
from os import listdir
from os.path import  join
import random
import threading

playing=False
first_time=True
window=Tk()

index=0
onlyfiles=[]
song_name=StringVar()
song_name.set('Choose a folder')

def browser():
    global file_dir
    global onlyfiles
    global player
    global index
    try:
        index=0
        onlyfiles=[""]
        file_dir=filedialog.askdirectory()
        player.stop()
        onlyfiles = [f for f in listdir(file_dir) if f.endswith('.mp3')]
        if(onlyfiles==[]):
            raise FileNotFoundError
        start()
    except(FileNotFoundError):
        if(file_dir==""):
            pass
        else:
            messagebox.showinfo('Error','No MP3 in selected folder select a folder with mp3 file')
player=MediaPlayer()
libvlc_audio_set_volume(player,70)
def start():
    global index
    global player
    global song_name
    global playing
    global first_time
    global t1
    try:
        song_name=onlyfiles[index].replace(".mp3","")
        label.configure(text=song_name)
        player=MediaPlayer(join(file_dir,onlyfiles[index]))
        player.play()
        playing = True
        first_time = False
        button2.configure(image=pausePh)
        t1=threading.Thread(target=position)
        t1.start()
    except(IndexError):
        index=0
        start()

def shuffling():
    global onlyfiles
    global index
    random.shuffle(onlyfiles)


#TODO Make the shuffle as a toggle as it supposed to be
def player_play(event=None):
    global index
    global player
    global song_name
    global playing
    global first_time

    if first_time:
        first_time=False
        start()
    elif playing:
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
def position():
    total_time=get_len(player)
    total_time=total_time/60000
    labelpos.configure(text=str(total_time))
    pos=get_pos(player)
    while pos<1 :
        pos=get_pos(player)
def vol_in():
    per=libvlc_audio_get_volume(player)
    per+=10
    if not per>=100:
        libvlc_audio_set_volume(player,per)
    else:
        pass
def vol_dec():
    per=libvlc_audio_get_volume(player)
    per-=10
    if not per<=0:
        libvlc_audio_set_volume(player,per)
    else:
        pass




# TODO Implement the volume increase and decrease


def swap_icon(temp):
    global varPh
    global pausePh
    global playPh
    if temp:
        varPh = pausePh
        button2.configure(image=varPh)
        button2.image = varPh
    else:
        varPh = playPh
        button2.configure(image=varPh)
        button2.image = varPh
window.title("MP3 Player")
window.configure(background="black")
window.geometry("300x120")

topFrame=Frame(window)
topFrame.pack(side=TOP)
bottomFrame=Frame(window)
bottomFrame.pack(side=TOP)
#Top Music Informations
label=Label(topFrame,text='Choose a Directory',fg='grey',bg='black',font='Roboto')
label.configure(font=('Roboto','16'),width=300)
label.pack()
labelpos=Label(topFrame,text='Start the music',fg='grey',bg='black')
labelpos.pack()
browse_button=Button(topFrame,text='Browse',font='Roboto',fg='#2ECC71',bg='black',command=browser)
browse_button.pack(fill=X)


#Media Button layout and design
playPh = PhotoImage(file='Images\\play.png')
nextPh = PhotoImage(file='Images\\next.png')
prevPh = PhotoImage(file='Images\\previous.png')
pausePh= PhotoImage(file='Images\\pause.png')


varPh=playPh


button1=Button(bottomFrame,image=prevPh,bg='black',height=10,width=40,command=prev)
button2=Button(bottomFrame,image=varPh,bg='black',height=10,width=40,command=player_play)
button3=Button(bottomFrame,image=nextPh,bg='black',height=10,width=40,command=next)
button4=Button(bottomFrame,text='Shuffle',bg='black',fg='grey',height=10,width=5,command=shuffling)
but_vol_in=Button(bottomFrame,text='+',bg='black',fg='grey',height=10,width=5,command=vol_in)
but_vol_de=Button(bottomFrame,text='-',bg='black',fg='grey',height=10,width=5,command=vol_dec)
button1.image=prevPh
button2.image=varPh
button3.image=nextPh


button1.pack(side=LEFT,fill=Y)
button2.pack(side=LEFT,fill=Y)
button3.pack(side=LEFT,fill=Y)
button4.pack(side=LEFT,fill=Y)
but_vol_in.pack(side=LEFT,fill=Y)
but_vol_de.pack(side=LEFT,fill=Y)

def on_closing():
    player.stop()
    window.destroy()


window.bind('<space>',player_play)
window.iconbitmap('Images\\icon.png')
window.protocol('WM_DELETE_WINDOW',on_closing)
window.mainloop()
