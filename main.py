import tkinter
import sys
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging


logger = logging.Logger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)


class GUI(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        if not kwargs.get("className"):
            kwargs["className"] = "eInk"
        super().__init__(*args, **kwargs)

        self.canvas = tkinter.Canvas(self, bg="white", width=600, height=800)
        self.canvas.pack()

    def parse_uart(self, uart):
        # TODO: replace with actual UART parsing
        self.canvas.delete("all")
        self.canvas.create_text((300, 400), text=uart, font=("Sans, 24"))


class UARTRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, gui, *args):
        self.gui = gui
        return super().__init__(*args)

    def do_GET(self):
        uart = self.path.replace("/", "")
        logger.info("Command received: " + uart)

        self.send_response(200)
        self.end_headers()
        # TODO: replace with correct UART responses
        self.wfile.write(uart.encode())

        self.gui.parse_uart(uart)


def start_http_server(httpd):
    logger.info("Starting HTTP server")
    httpd.serve_forever()
    logger.info("HTTP server terminated gracefully")


if __name__ == "__main__":
    gui = GUI()

    def create_http_handler(*args):
        return UARTRequestHandler(gui, *args)

    httpd = HTTPServer(("localhost", 9999), create_http_handler)

    server = threading.Thread(target=start_http_server, args=(httpd,))
    server.start()
    gui.mainloop()
    httpd.shutdown()
