import tkinter as tk
from tkinter import ttk

class FlashcardEditor(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller