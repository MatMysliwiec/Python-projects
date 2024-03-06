import curses
import socket
import threading


class Whiteboard:
    def __init__(self, stdscr, host, port):
        self.stdscr = stdscr
        self.host = host
        self.port = port
        self.messages = []
        self.lock = threading.Lock()

        self.init_curses()
        self.init_network()

    def init_curses(self):
        start_color()
        init_pair(1, COLOR_BLACK, COLOR_WHITE)
        self.stdscr.clear()
        self.stdscr.refresh()
        self.stdscr.keypad(True)

    def init_network(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.stdscr.addstr(0, 0, f"Server listening on {self.host}:{self.port}")
        self.stdscr.refresh()

    def accept_connections(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket)).start()

    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                with self.lock:
                    self.messages.append(data)
                    self.redraw()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

    def redraw(self):
        self.stdscr.clear()

        for idx, message in enumerate(self.messages):
            self.stdscr.addstr(idx + 1, 0, message, color_pair(1))

        self.stdscr.refresh()

    def run(self):
        threading.Thread(target=self.accept_connections()).start()

        while True:
            key = self.stdscr.getch()
            if key == ord('q'):
                break

            if KEY_MOUSE:
                try:
                    _, mx, my, _, _ = getmouse()
                    self.stdscr.addstr(my, mx, 'X', color_pair(1))
                    self.stdscr.refresh()

                    with self.lock:
                        self.messages.append(f"Draw at {mx}, {my}")
                        self.redraw()
                except:
                    pass


if __name__ == "__main__":
    host = ""
    port = 5585

    stdscr = initscr()
    mousemask(1)
    curs_set(0)
    noecho()

    whiteboard = Whiteboard(stdscr, host, port)
    whiteboard.run()

    endwin()
