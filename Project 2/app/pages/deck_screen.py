import tkinter as tk


class DeckScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.buttons = []
        self.selected_button = None
        
        # UI Setup
        label = tk.Label(self, text="PyFlash", font=("Arial", 24))
        label.pack(pady=10)
        
        # Control Buttons
        control_frame = tk.Frame(self)
        control_frame.pack(pady=10)
        
        tk.Button(control_frame, text="Add Deck", command=self.add_deck).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Edit Deck", command=self.edit_deck).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Remove Deck", command=self.remove_deck).pack(side=tk.LEFT, padx=5)
        
        # Scrollable Deck Area
        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)
        
        self.scrollable_frame.bind("<Configure>", 
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Add sample decks
        for i in range(3):
            self.add_deck(f"Sample Deck {i+1}")
    
    def add_deck(self, text=None):
        """Add a new deck button"""
        if not text:
            text = f"Sample Deck {len(self.buttons)+1}"
            
        btn = tk.Button(
            self.scrollable_frame,
            text=text,
            bg="SystemButtonFace",
            width=20
        )
        
        # Use a wrapper function to avoid lambda issues
        def make_command(button):
            return lambda: self.modify_button(button)
        
        btn.config(command=make_command(btn))
        btn.pack(fill=tk.X, pady=5)
        self.buttons.append(btn)
    
    def modify_button(self, button):
        """Handle deck selection"""
        if self.selected_button:
            self.selected_button.config(bg="SystemButtonFace", relief=tk.RAISED)
        button.config(bg="#4b8bbe", fg="#0000FF", relief=tk.SUNKEN)
        self.selected_button = button
    
    def edit_deck(self):
        if self.selected_button:
            print(f"Editing {self.selected_button.cget('text')}")
    
    def remove_deck(self):
        if self.selected_button and self.selected_button in self.buttons:
            self.buttons.remove(self.selected_button)
            self.selected_button.destroy()
            self.selected_button = None

