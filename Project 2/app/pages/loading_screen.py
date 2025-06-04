import tkinter as tk
from tkinter import ttk

class LoadingScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="PyFlash", font=("Arial", 50))
        label.pack(pady=60)

        label1 = tk.Label(self, text="Loading...", font=('Ariel', 16))
        label1.pack(pady=40)

        self.progress = ttk.Progressbar(self, mode='indeterminate')
        self.progress.pack(fill=tk.X, padx=20)

        self.start_loading()
    
    def start_loading(self):
        self.progress.start(10)
    def stop_loading(self):
        self.progress.stop()