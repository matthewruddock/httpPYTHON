from tkinter import*
from tkinter import messagebox #import messagebox library
import dashboard as db

######FUNCTIONS######
def submitLogin():
    username = userEntry.get()
    password = pwdEntry.get()
    print("Username = ",username)
    print("Password = ",password)
    if(username=="admin")and (password=="ASPIRE22"):
        loginWindow.destroy()
        db.main()
    else:
        messagebox.showerror(title='ERROR', message='Incorrect Username/Password Entered\n\n Please Try Again')
    
def infoMenu():
    messagebox.showinfo(title='Info', message='         Copyright to ASIPIRE \n\n               March 31, 2022 \n\n                 Made by: \n\n           Matthew Ruddock,\n            Gabrielle Hydol, \n            Jamahli Mitchell,\n            Ricardo Barrett')



######WINDOW######

#Window for Login
loginWindow = Tk() #instantiate an instance of a window
loginWindow.geometry("550x400") #size of window
loginWindow.title("ASPIRE HTTP PROXY") # set title of window
windowIconImage = PhotoImage(file='httpPYTHON\\imgs\\server.png') #creates window icon
loginWindow.iconphoto(True,windowIconImage) #sets window icon
loginWindow.config(background="light blue") #sets background color for window...can use hex value as well

######IMAGES######
infoImage = PhotoImage(file="httpPYTHON\\imgs\\info.png")
exitImage = PhotoImage(file="httpPYTHON\\imgs\\exit.png")
programImage = PhotoImage(file="httpPYTHON\\imgs\\server.png")



######MENU BAR######
menubar = Menu(loginWindow)  #Creates a Menubar
loginWindow.config(menu=menubar) #Add menubar to the window

#File Menu
fileMenu = Menu(menubar, tearoff=0, font=("Times",10))
menubar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Info",command=infoMenu, image=infoImage, compound='right')
fileMenu.add_command(label="Exit ", command=quit, image=exitImage, compound='right')





######LABELS######
loginLabel = Label(
    text=" ASPIRE HTTP PROXY LOGIN",
    font=("Arial",20),
    bg="white",fg="black",
    image=programImage,compound='left'
)
loginLabel.place(x=60,y=40) #place label at an pixel axis

userLabel = Label(
    text="Username:",
    font=("Arial",14),
)
userLabel.place(x=100,y=140) #place label at an pixel axis

pwdLabel = Label(
    text="Password:",
    font=("Arial",14),
)
pwdLabel.place(x=100,y=190) #place label at an pixel axis




######ENTRY######
userEntry = Entry(loginWindow,
                font=("Arial",14),
                fg="blue",
                
                )
userEntry.insert(0,'username') #Set Default string in entry window
userEntry.place(x=200,y=140)


pwdEntry = Entry(loginWindow,
                font=("Arial",14),
                fg="blue",
                show="*"
                
                )
pwdEntry.insert(0,'password') #Set Default string in entry window
pwdEntry.place(x=200,y=190)





######BUTTONS######
submit_button = Button(loginWindow, text="SUBMIT", command=submitLogin,font=("Arial",14),bg="blue",fg="white",activeforeground="black", activebackground="white",)
submit_button.place(x=200,y=240)








loginWindow.mainloop() #place window on computer screen, listen for events

