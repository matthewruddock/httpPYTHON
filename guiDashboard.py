#Developers:   Matthew Ruddock(1700241), Gabrielle Hydol(1901163),  Jamahli Mitchell,  Ricardo Barrett
from tkinter import*
from tkinter import messagebox #import messagebox libraryr
from tkinter import ttk
import time, sys, multiprocessing, subprocess
import proxyServer as ps


def main():
    global serverFlag
    serverFlag = 0
    global startTime
    startTime = time.perf_counter()

    ######FUNCTIONS######
    def infoMenu():
        messagebox.showinfo(title='Info', 
                            message='         Copyright to ASIPIRE \n\n               March 31, 2022 \n\n                 Made by: \n\n           Matthew Ruddock,\n            Gabrielle Hydol, \n            Jamahli Mitchell,\n            Ricardo Barrett')

    ######WINDOW######

    #Window for Dashboard
    dashboardWindow = Tk() #instantiate an instance of a window
    dashboardWindow.geometry("800x500") #size of window
    dashboardWindow.title("ASPIRE HTTP PROXY") # set title of window
    dashboardWindow.resizable(width=False, height=False)
    windowIconImage = PhotoImage(file='httpPYTHON\\imgs\\server.png') #creates window icon
    dashboardWindow.iconphoto(True,windowIconImage) #sets window icon
    dashboardWindow.config(background="light blue",borderwidth=5, relief="solid") #sets background color for window...can use hex value as well


    ######IMAGES######
    infoImage = PhotoImage(file="httpPYTHON\\imgs\\info.png")
    exitImage = PhotoImage(file="httpPYTHON\\imgs\\exit.png")
    programImage = PhotoImage(file="httpPYTHON\\imgs\\server.png")
    startServerImage = PhotoImage(file="httpPYTHON\\imgs\\server_online.png")
    stopServerImage = PhotoImage(file="httpPYTHON\\imgs\\server_shutdown.png")
    monitoringImage = PhotoImage(file="httpPYTHON\\imgs\\monitoring.png")
    BlacklistImage = PhotoImage(file="httpPYTHON\\imgs\\lock_50.png")
    BlacklistIpImage = PhotoImage(file="httpPYTHON\\imgs\\iplock_50.png")
    BackgroundImage = PhotoImage(file="httpPYTHON\\imgs\\b1.png",)




    ######MENU BAR######
    menubar = Menu(dashboardWindow)  #Creates a Menubar
    dashboardWindow.config(menu=menubar) #Add menubar to the window

    #File Menu
    fileMenu = Menu(menubar, tearoff=0, font=("Times",10))
    menubar.add_cascade(label="File", menu=fileMenu)

    fileMenu.add_command(label="Info",command=infoMenu, image=infoImage, compound='right')
    fileMenu.add_command(label="Exit ", command=sys.exit, image=exitImage, compound='right')




    ######LABELS######
    dashboardLabel = Label(text=" ASPIRE HTTP PROXY Dashboard ",
                            font=("Arial",20),
                            bg="white",fg="black",
                            image=programImage,compound='left',
                            borderwidth=2, relief="solid"
                        )

    dashboardLabel.place(x=180,y=40) #place label at an pixel axis

    backgroundLabel = Label( image=BackgroundImage,compound='left')
    
    backgroundLabel.place(x=300,y=140)




    ######BUTTONS######

    #shows Netowrk Traffic Button
    netowrkTrafficButton = Button(
                text="Network Traffic",
                command=netowrkTrafficData,
                font=("Comic Sans",14),
                fg="white",
                bg="dark green",
                activeforeground="black",
                activebackground="yellow",
                image=monitoringImage,
                compound='right') 
    netowrkTrafficButton.place(x=50,y=130)

    #shows Start Server Button
    startServerButton = Button(
                text="Start Server",
                command=startServer,
                font=("Comic Sans",14),
                fg="white",
                bg="dark green",
                activeforeground="black",
                activebackground="yellow",
                image=startServerImage,
                compound='right') 
    startServerButton.place(x=50,y=200)

    #shows Stop Server Button
    stopServerButton = Button(
                text="Stop Server",
                command=stopServer,
                font=("Comic Sans",14),
                fg="white",
                bg="dark red",
                activeforeground="black",
                activebackground="yellow",
                image=stopServerImage,
                compound='right') 
    stopServerButton.place(x=50,y=275)

    #shows Blacklist URL Button
    blacklistURLButton = Button(
                text="Blacklist URL Filter",
                command=enableBlacklistURL,
                font=("Comic Sans",14),
                fg="black",
                bg="#F7E11E",
                activeforeground="black",
                activebackground="yellow",
                image=BlacklistImage,
                compound='right') 
    blacklistURLButton.place(x=50,y=350)

    #shows Blacklist IP Button
    blacklistIPButton = Button(
                text="Blacklist IP Filter",
                command=enableBlacklistIP,
                font=("Comic Sans",14),
                fg="black",
                bg="#F7E11E",
                activeforeground="black",
                activebackground="yellow",
                image=BlacklistIpImage,
                compound='right') 
    blacklistIPButton.place(x=50,y=425)


    dashboardWindow.mainloop() #place window on computer screen, listen for events
###### COMMANDS ######
def startServer():
        global serverFlag 
        serverFlag = 1

        messagebox.showwarning(title='Server Status', message='Server has Started')

        process1 = multiprocessing.Process(target=ps.Server)
        process1.start()


def stopServer():
        global serverFlag
        global server

        if(serverFlag==1):
            messagebox.showinfo(title='Server Status', message='Server was Shutdown Successfully')
            ps.Server.stop_server
        else:
            messagebox.showerror(title='ERROR', message='ERROR: Server was not enabled ')
    
def enableBlacklistIP():
        
        #Submit Command
        def blacklistFilterListBox_Submit():
            ip = []

            for index in blacklistFilter_listbox.curselection():
                ip.insert(index, blacklistFilter_listbox.get(index))
  
            blacklistFile = open("httpPYTHON\\log\\blacklistIP.txt","w")
            blacklistFile.close()

            print("You have selected: ")
           
            for index in ip:
                print(index)
                with open("httpPYTHON\\log\\blacklistIP.txt","a") as blacklistFile:
                    blacklistFile.writelines(index+"\n")

            messagebox.showwarning(title='Blacklist Status', message='Blacklist IP Filter has been Updated')

        #Add Command
        def blacklistFilterListBox_Add():
            blacklistFilter_listbox.insert(blacklistFilter_listbox.size(), entryBox.get())
            blacklistFilter_listbox.config(height=blacklistFilter_listbox.size())
            
        #Delete Command
        def blacklistFilterListBox_Delete():
            for index in reversed(blacklistFilter_listbox.curselection()):
                blacklistFilter_listbox.delete(index)
            
            blacklistFilter_listbox.config(height=blacklistFilter_listbox.size())

        print(" blacklist filter opened")

        #Blacklist Window
        blacklistFilterWindow = Toplevel() 
        blacklistFilterWindow.title("Blacklist IP Filter")
        blacklistFilterWindow.geometry("400x300")
        blacklistFilterWindow.config(background="light blue")

        #Blacklist Frame
        blacklistFrame = Frame(blacklistFilterWindow, highlightbackground="blue", highlightthickness=2)
        blacklistFrame.pack(padx=10, pady=10)

        blacklistLabel = Label(blacklistFrame,text=" Blacklist IP Filter ",
                            font=("Arial",20),
                            fg="black", bg="#1EA7F7",
                            borderwidth=2, relief="raised"
                        )

        blacklistLabel.grid(row=0,column=0,pady=10,columnspan=2)

        #Blacklist Listbox
        blacklistFilter_listbox = Listbox(blacklistFrame,
                                    font = ("Times", 12),
                                    width=12,
                                    bg="black",
                                    fg="white",
                                    selectmode=MULTIPLE
                                    )
        blacklistFilter_listbox.grid(row=2,column=0,padx=10,pady=10,columnspan=2)

        #Default listings
        try:
            blacklistFile = open("httpPYTHON\\log\\blacklistIP.txt","r")

            for ip in blacklistFile.readlines():
                print(ip)
                blacklistFilter_listbox.insert(END,ip)
        finally:
            blacklistFile.close()

        #blacklistFilter_listbox.insert(1,"facebook")
        #blacklistFilter_listbox.insert(2,"jamaica-gleaner")
        #blacklistFilter_listbox.insert(3,"yahoo")
        blacklistFilter_listbox.config(height=blacklistFilter_listbox.size(), width=40)

        entryBox = Entry(blacklistFrame, width=20)
        entryBox.grid(row=3,column=0,pady=10,columnspan=2)

        submitButton = Button(blacklistFrame, text="Submit", command=blacklistFilterListBox_Submit)
        submitButton.grid(row=4,column=0,padx=5,pady=5,columnspan=2)

        addButton = Button(blacklistFrame, text="Add", command=blacklistFilterListBox_Add)
        addButton.grid(row=5,column=0)

        deleteButton = Button(blacklistFrame, text="Delete", command=blacklistFilterListBox_Delete)
        deleteButton.grid(row=5,column=1)

        blacklistFilterWindow.mainloop()

def enableBlacklistURL():

        #Submit Command
        def blacklistFilterListBox_Submit():
            websites = []

            for index in blacklistFilter_listbox.curselection():
                websites.insert(index, blacklistFilter_listbox.get(index))
  
            blacklistFile = open("httpPYTHON\\log\\blacklistURL.txt","w")
            blacklistFile.close()

            print("You have selected: ")
           
            for index in websites:
                print(index)
                with open("httpPYTHON\\log\\blacklistURL.txt","a") as blacklistFile:
                    blacklistFile.writelines(index+"\n")

            messagebox.showwarning(title='Blacklist Status', message='Blacklist URL filter has been Updated')

        #Add Command
        def blacklistFilterListBox_Add():
            blacklistFilter_listbox.insert(blacklistFilter_listbox.size(), entryBox.get())
            blacklistFilter_listbox.config(height=blacklistFilter_listbox.size())
            

        #Delete Command
        def blacklistFilterListBox_Delete():
            for index in reversed(blacklistFilter_listbox.curselection()):
                blacklistFilter_listbox.delete(index)
            
            blacklistFilter_listbox.config(height=blacklistFilter_listbox.size())

        print(" blacklist filter opened")

        #Blacklist Window
        blacklistFilterWindow = Toplevel() 
        blacklistFilterWindow.title("Blacklist URL Filter")
        blacklistFilterWindow.geometry("400x300")
        blacklistFilterWindow.config(background="light blue")

        #Blacklist Frame
        blacklistFrame = Frame(blacklistFilterWindow, highlightbackground="blue", highlightthickness=2)
        blacklistFrame.pack(padx=10, pady=10)

        blacklistLabel = Label(blacklistFrame,text=" Blacklist URL Filter ",
                            font=("Arial",20),
                            fg="black", bg="#1EA7F7",
                            borderwidth=2, relief="raised"
                        )

        blacklistLabel.grid(row=0,column=0,pady=10,columnspan=2)

        #Blacklist Listbox
        blacklistFilter_listbox = Listbox(blacklistFrame,
                                    font = ("Times", 12),
                                    width=12,
                                    bg="black",
                                    fg="white",
                                    selectmode=MULTIPLE
                                    )
        blacklistFilter_listbox.grid(row=2,column=0,padx=10,pady=10,columnspan=2)

        #Default listings
        try:
            blacklistFile = open("httpPYTHON\\log\\blacklistURL.txt","r")

            for websites in blacklistFile.readlines():
                print(websites)
                blacklistFilter_listbox.insert(END,websites)

        finally:
            blacklistFile.close()

        #blacklistFilter_listbox.insert(1,"facebook")
        #blacklistFilter_listbox.insert(2,"jamaica-gleaner")
        #blacklistFilter_listbox.insert(3,"yahoo")
        blacklistFilter_listbox.config(height=blacklistFilter_listbox.size(), width=40)

        entryBox = Entry(blacklistFrame, width=20)
        entryBox.grid(row=3,column=0,pady=10,columnspan=2)

        submitButton = Button(blacklistFrame, text="Submit", command=blacklistFilterListBox_Submit)
        submitButton.grid(row=4,column=0,padx=5,pady=5,columnspan=2)

        addButton = Button(blacklistFrame, text="Add", command=blacklistFilterListBox_Add)
        addButton.grid(row=5,column=0)

        deleteButton = Button(blacklistFrame, text="Delete", command=blacklistFilterListBox_Delete)
        deleteButton.grid(row=5,column=1)

        blacklistFilterWindow.mainloop()

def netowrkTrafficData():
        time.sleep(1)
        networkTrafficWindow = Toplevel() #instantiate an instance of a window
        networkTrafficWindow.geometry("1400x500") #size of window
        networkTrafficWindow.title("Network Traffic") # set title of window
        networkTrafficWindow.resizable(True, False)

        networkTrafficWindow.config(background="grey") #sets background color for window...can use hex value as well

        # apply the grid layout
        networkTrafficWindow.grid_columnconfigure(0, weight=1)
        networkTrafficWindow.grid_rowconfigure(0, weight=1)

        # create the text widget
        networkTrafficText = Text(networkTrafficWindow, height=30,width=100,bg="black",fg="white",font="Times, 10")
        networkTrafficText.grid(row=0, column=0, sticky='ew')

        # create a scrollbar widget and set its command to the text widget
        scrollbarVertical = ttk.Scrollbar(networkTrafficWindow, orient='vertical', command=networkTrafficText.yview)
        scrollbarVertical.grid(row=0, column=1, sticky='ns')

        #communicate back to the scrollbar
        networkTrafficText['yscrollcommand'] = scrollbarVertical.set

        try:
            logFile = open("httpPYTHON\\log\\proxyServerLog.txt","r")

            for logLine in logFile.readlines():
                networkTrafficText.insert('1.0',logLine)
        finally:
            logFile.close()
        
        networkTrafficWindow.mainloop() #place window on computer screen, listen for events

        

if __name__ == "__main__":
    main()
    