import tkinter as tk 
from .pages.loading_screen import LoadingScreen
from .pages.deck_screen import DeckScreen
import time
import threading

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyFlash")
        self.geometry("820x480")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.loading_screen = LoadingScreen(self.container, self)
        self.loading_screen.pack(fill="both", expand=True)

        self.after(100, self.simulate_loading)
    def simulate_loading(self):
        def load_data():
            time.sleep(2)
            self.after(0, self.show_deck_screen)
        threading.Thread(target=load_data, daemon=True).start()
    def show_deck_screen(self):
        self.loading_screen.stop_loading()
        self.loading_screen.pack_forget()
        self.desk_screen = DeckScreen(self.container, self)
        self.desk_screen.pack(fill="both", expand=True)
        



if __name__ == "__main__":
    app = App()
    app.mainloop()
