global serverFlag
serverFlag = 5
blacklistFlag = 0

def main():

    def startServer():
        global serverFlag
        print("start server flag: ")
        print(serverFlag)
        serverFlag = 1

    def stopServer():
        global serverFlag
        if(serverFlag==1):
            print("stop server flag: ")
            print(serverFlag)
    
    startServer()
    stopServer()

if __name__ == "__main__":
    main()