#Developers:   Matthew Ruddock(1700241), Gabrielle Hydol(1901163),  Jamahli Mitchell(1800994),  Ricardo Barrett(1903452)
#Class Occurrence: LAB Monday 2PM

KNOWN BUGS: - Dashbaord GUI crashes when trying to close, after running Server.
            - Login GUI is prompt twice after running Server
            - Blacklisting works by entering www.(webstite).com .. For example, www.yahoo.com or www.jamaica-gleaner.com

Go to Web Browser (Recommended FireFox):
    - Go to Network settings
    - Enter 127.0.0.1 in HTTP Proxy
    - Enter 8000 in Port

Start Program by Running the "guiLogin.py"

In the Login
    - Enter 'admin' for username and 'ASPIRE22' for password
    - User will be directed to the Dashboard

In the Dashboard (guiDashboard)
    - Select "Start Server" Button to run the server
    - Select "Stop Server" Button to stop the server
    - Select "Network Traffic" Button to view the Traffic ont the Network
    - Select "Blacklist URL Filter" Button to add, edit or view the URL which should be Blacklisted.
    - Select "Blacklist IP Filter" Button to add, edit or view the IPs which should be Blacklisted.
    - The Dashboard can be exited from the "Exit" command found in the Menu Bar below "File"

Entering Blacklist URL Filter
    - To add the domain to the blacklist, enter only the domain name of the website. The followng are not allowed: www, net, com, org
    - To delete the domain, select the domains and click the "Delete" button.
    - To submit the domain, select all the domains and click the "Submit" button.

Entering Blacklist IP Filter
    - To add the IP ADDRESS to the blacklist, enter only the IP ADDRESS. The followng are not allowed: www, net, com, org
    - To delete the IP ADDRESS, select the IP ADDRESS and click the "Delete" button.
    - To submit the IP ADDRESS, select all the IP ADDRESS and click the "Submit" button.

NOTE: Server has to be stopped by using "Ctrl + C" in the terminal.

