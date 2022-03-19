from tkinter import*
from tkinter import messagebox #import messagebox library
from tkinter import ttk


def main():
    global serverFlag
    global blacklistFlag

    serverFlag = 0
    blacklistFlag = 0

    ######FUNCTIONS######
    def infoMenu():
        messagebox.showinfo(title='Info', message='         Copyright to ASIPIRE \n\n               March 31, 2022 \n\n                 Made by: \n\n           Matthew Ruddock,\n            Gabrielle Hydol, \n            Jamahli Mitchell,\n            Ricardo Barrett')

    def startServer():
        global serverFlag 
        print("starting server")
        serverFlag = 1
        messagebox.showwarning(title='Server Status', message='Server has Started')
        netowrkTrafficData()

    def stopServer():
        global serverFlag
        if(serverFlag==1):
            print("shutting down server")
            messagebox.showinfo(title='Server Status', message='Server was Shutdown Successfully')
        else:
            messagebox.showerror(title='ERROR', message='ERROR: Server was not enabled ')
    
    def enableBlacklist():
        global blacklistFlag
        print("enabling blacklist")
        blacklistFlag = 1
        messagebox.showwarning(title='Blacklist Status', message='Blacklisting is Enabled')

    def disableBlacklist():
        global blacklistFlag
        if(blacklistFlag==1):
            print("disable blacklist")
            messagebox.showinfo(title='Blacklist Status', message='Blacklisting is Disabled')
        else:
            messagebox.showerror(title='ERROR', message='ERROR: Blacklist was not enabled ')

    
    def netowrkTrafficData():
        networkTrafficWindow = Tk()
        networkTrafficWindow.resizable(False, False)
        networkTrafficWindow.title("Network Traffic")

        # apply the grid layout
        networkTrafficWindow.grid_columnconfigure(0, weight=1)
        networkTrafficWindow.grid_rowconfigure(0, weight=1)

        # create the text widget
        networkTrafficText = Text(networkTrafficWindow, height=50,width=150)
        networkTrafficText.grid(row=0, column=0, sticky='ew')

        # create a scrollbar widget and set its command to the text widget
        scrollbar = ttk.Scrollbar(networkTrafficWindow, orient='vertical', command=networkTrafficText.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')

        #  communicate back to the scrollbar
        networkTrafficText['yscrollcommand'] = scrollbar.set

        networkTrafficText.insert('1.0','The Text widget allows you to display \nand edit multi-line textarea with various styles. Besides the plain text, the Text widget supports embedded images and links.\nTo create a text widget, you use the following syntax:')
        networkTrafficWindow.mainloop()


    ######WINDOW######

    #Window for Dashboard
    dashboardWindow = Tk() #instantiate an instance of a window
    dashboardWindow.geometry("1000x500") #size of window
    dashboardWindow.title("ASPIRE HTTP PROXY") # set title of window
    windowIconImage = PhotoImage(file='httpPYTHON\\imgs\\server.png') #creates window icon
    dashboardWindow.iconphoto(True,windowIconImage) #sets window icon
    dashboardWindow.config(background="light blue") #sets background color for window...can use hex value as well


    ######IMAGES######
    infoImage = PhotoImage(file="httpPYTHON\\imgs\\info.png")
    exitImage = PhotoImage(file="httpPYTHON\\imgs\\exit.png")
    programImage = PhotoImage(file="httpPYTHON\\imgs\\server.png")
    startServerImage = PhotoImage(file="httpPYTHON\\imgs\\server_online.png")
    stopServerImage = PhotoImage(file="httpPYTHON\\imgs\\server_shutdown.png")
    monitoringImage = PhotoImage(file="httpPYTHON\\imgs\\server_online.png")
    enableBlacklistImage = PhotoImage(file="httpPYTHON\\imgs\\lock_50.png")
    disableBlacklistImage = PhotoImage(file="httpPYTHON\\imgs\\unlock_50.png")



    ######MENU BAR######
    menubar = Menu(dashboardWindow)  #Creates a Menubar
    dashboardWindow.config(menu=menubar) #Add menubar to the window

    #File Menu
    fileMenu = Menu(menubar, tearoff=0, font=("Times",10))
    menubar.add_cascade(label="File", menu=fileMenu)

    fileMenu.add_command(label="Info",command=infoMenu, image=infoImage, compound='right')
    fileMenu.add_command(label="Exit ", command=quit, image=exitImage, compound='right')







    ######LABELS######
    dashboardLabel = Label(text=" ASPIRE HTTP PROXY Dashboard ",
                            font=("Arial",20),
                            bg="white",fg="black",
                            image=programImage,compound='left',
                        )

    dashboardLabel.place(x=250,y=40) #place label at an pixel axis

    functionsLabel = Label(text="-CONTROLS-",
                            font=("Arial",20),
                            fg="black", bg="white",
                            borderwidth=2, relief="ridge"
                        )

    functionsLabel.place(x=40,y=140) #place label at an pixel axis





    ######BUTTONS######
    startServerButton = Button(
                text="Start Server",
                command=startServer,
                font=("Comic Sans",14),
                fg="white",
                bg="dark blue",
                activeforeground="black",
                activebackground="yellow",
                image=startServerImage,
                compound='right') 
    startServerButton.place(x=40,y=200)

    stopServerButton = Button(
                text="Stop Server",
                command=stopServer,
                font=("Comic Sans",14),
                fg="white",
                bg="dark blue",
                activeforeground="black",
                activebackground="yellow",
                image=stopServerImage,
                compound='right') 
    stopServerButton.place(x=40,y=275)

    enableBlacklistButton = Button(
                text="Enable Blacklist",
                command=enableBlacklist,
                font=("Comic Sans",14),
                fg="white",
                bg="dark blue",
                activeforeground="black",
                activebackground="yellow",
                image=enableBlacklistImage,
                compound='right') 
    enableBlacklistButton.place(x=40,y=350)

    disableBlacklistButton = Button(
                text="Disable Blacklist",
                command=disableBlacklist,
                font=("Comic Sans",14),
                fg="white",
                bg="dark blue",
                activeforeground="black",
                activebackground="yellow",
                image=disableBlacklistImage,
                compound='right') 
    disableBlacklistButton.place(x=40,y=425)


    ######TEXT######


    dashboardWindow.mainloop() #place window on computer screen, listen for events

if __name__ == "__main__":
    main()