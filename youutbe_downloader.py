from tkinter import *
from tkinter import filedialog
import youtube_dl
import os

windows=Tk()
windows.configure(background='Lightgoldenrod2')
windows.geometry('1280x720')

folder_path = StringVar()
def clear():
    en1.delete(first=0,last=100)

def sel_folder():
    global filname
    global folder_path
    filename=filedialog.askdirectory()
    folder_path.set(filename)

def downl():
    URl = en1.get()
    PATH = en2.get()
    yd_dic = {}
    os.chdir(PATH)
    with youtube_dl.YoutubeDL(yd_dic) as ydl:
        windows.title =('Downloading...' + URl )
        ydl.download([URl])
    print(yd_dic)
    noty = "your video is downloaded"
    windows.title(noty)
    Notification.configure(text=noty, fg='black', bg="SpringGreen3", width=50, font=('times', 17, 'bold', 'italic'))
    Notification.place(x=430, y=600)


lb1 = Label(windows,width=20,text='Youtube Video Downloader',fg ='Black',bg='Lightgoldenrod2',font=('times',30,'bold'))
lb1.place(x=430,y=50)

lb2 = Label(windows,width=12,height=2,text='Youtube-Link',fg ='Black',bg='goldenrod1',font=('times',25,'bold'))
lb2.place(x=150,y=200)

en1 = Entry(windows,width=15,fg ='Black',bg='tan1',font=('times',50,'italic'))
en1.place(x=450,y=200)

clearbt = Button(windows,width=12,height=2,command=clear,text='Clear',fg ='Black',bg='gold',font=('times',18,'bold'))
clearbt.place(x=1000,y=200)

lb3 = Label(windows,width=12,height=2,text='Folder',fg ='Black',bg='goldenrod1',font=('times',25,'bold'))
lb3.place(x=150,y=300)

en2 = Entry(windows,width=15,text=folder_path,fg ='Black',bg='tan1',font=('times',50,'italic'))
en2.place(x=450,y=300)

selectbtn = Button(windows,width=12,height=2,command=sel_folder,text='Select-Folder',fg ='Black',bg='gold',font=('times',18,'bold'))
selectbtn.place(x=1000,y=300)

down = Button(windows,width=20,height=1,text='Download',command=downl   ,fg ='Black',bg='orange',font=('times',18,'bold'))
down.place(x=530,y=450)

bottom = Label(windows,width=120,height=1,text='© Rohit Sainik',fg ='Black',bg='snow',font=('times',15,'bold'))
bottom.place(x=00,y=650)

Notification = Label(windows, text="Video downloaded", bg="snow", fg="white", width=35,height=3, font=('times', 17, 'bold'))

windows.mainloop()