import dearpygui.dearpygui as dpg
#import blocker as blockerUrl
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

#SERVER
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

def stop():
    run.httpd.server_close()
    logging.info('Stopping httpd...\n')












#GUI
dpg.create_context()


#startServer buttion function
def btn_callback_startServer():
    print("Server has Started")
    run()

#stopServer buttion function
def btn_callback_stopServer():
    print("Server has stopped")
    stop()


#startBlockerURLs buttion function
def btn_callback_startBlockerURLs(sender, app_data, user_data):
    print("Blocker has started")

#stopBlockerURLs buttion function
def btn_callback_stopBlockerURLs(sender, app_data, user_data):
    print("Blocker has stopped")

#exits the program
def exitProgram():
    dpg.destroy_context()



#Windows
with dpg.window(tag="ASPIRE HTTP Proxy Server"):
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Info", callback=lambda: dpg.configure_item("modal_id", show=True))
            dpg.add_menu_item(label="Exit", callback=exitProgram)
    dpg.add_text("Server Address: http://127.0.0.1:8000/")
    dpg.add_button(label="Start Server", callback=btn_callback_startServer)
    dpg.add_button(label="Stop Server", callback=btn_callback_stopServer)
    dpg.add_text(" ")
    dpg.add_button(label="Start Block URLs", callback=btn_callback_startBlockerURLs)
    dpg.add_button(label="Stop Block URLs", callback=btn_callback_stopBlockerURLs)

#network traffic window
with dpg.window(label="Netowrk Traffic", width=500, height=800):
        dpg.add_text("Hello, world")

#client ip window
with dpg.window(label="Client IPs", width=300, height=300):
        dpg.add_text("Hello, world")

#program info window
with dpg.window(label="Info Program", modal=True, show=False, id="modal_id", no_title_bar=True):
        dpg.add_text("Copyright to ASIPIRE | March 31, 2022 | Made by: Matthew Ruddock, Gabrielle Hydol, Jamahli Mitchell, Ricardo Barrett")
        dpg.add_separator()
        with dpg.group(horizontal=True):
            dpg.add_button(label="Close", callback=lambda: dpg.configure_item("modal_id", show=False))



dpg.create_viewport(title='ASPIRE HTTP Proxy Server', width=900, height=900)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("ASPIRE HTTP Proxy Server", True)
dpg.start_dearpygui()
dpg.destroy_context()