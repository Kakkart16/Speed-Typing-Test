import tkinter as tk
from tkinter import ttk
import time
import threading
import random
from tkinter import PhotoImage
from text import easySentence, mediumSentence, hardSentence

class TypeSpeedGUI:
    
    # level = "easy"
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Appliacation")
        self.root.geometry("800x600")
        
        self.root.configure(bg="#323437")
        
        img = PhotoImage(file='gundam.png')
        self.root.iconphoto(True, img)
        
        self.frame = tk.Frame(self.root, bg="#323437")
        
        
        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("easy")
        
        difficulty_menu = ttk.Combobox(self.frame, textvariable=self.difficulty_var, values=["easy", "medium", "hard"])
        difficulty_menu.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky="E")
        difficulty_menu.bind("<<ComboboxSelected>>", self.changeDifficulty)
        
        # Create horizontal radio buttons
        # easy_button = tk.Radiobutton(self.frame, text="Easy", variable=self.difficulty_var, value="easy", command=self.changeDifficulty, font=("Helvetica", 12), bg="#323437", fg="#d1d0c5")
        # easy_button.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        # medium_button = tk.Radiobutton(self.frame, text="Medium", variable=self.difficulty_var, value="medium", command=self.changeDifficulty, font=("Helvetica", 12), bg="#323437", fg="#d1d0c5")
        # medium_button.grid(row=0, column=1, padx=5, pady=10, sticky="W")
        
        # hard_button = tk.Radiobutton(self.frame, text="Hard", variable=self.difficulty_var, value="hard", command=self.changeDifficulty, font=("Helvetica", 12), bg="#323437", fg="#d1d0c5")
        # hard_button.grid(row=0, column=2, padx=5, pady=10, sticky="W")
        
        # self.frame.columnconfigure(0, weight=1)
        # self.frame.columnconfigure(1, weight=1)
        # self.frame.columnconfigure(2, weight=1)
        
        
        self.sample_label = tk.Label(self.frame, text="", font=("Helvetica", 18),fg = "#d1d0c5", bg="#323437", wraplength=600, justify="center")
        self.sample_label.grid(row=1, column=0, columnspan=2, padx=5, pady=30)
        self.randomSentence()
        
        self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 24), bg="#c0c0c0")
        self.input_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=20, ipadx=10, ipady=10)
        self.input_entry.bind("<KeyRelease>", self.start)
        
        self.speed_label = tk.Label(self.frame, text="Speed: 0.00 CPS 0.00 CPM 0.00 WPS 0.00 WPM", font=("Helvectica", 18), fg = "#d1d0c5", bg="#323437")
        self.speed_label.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, font=("Helvetica", 12),bg="#c0c0c0")
        self.reset_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
        
        self.frame.pack(expand=True)
        
        self.counter = 0
        self.running = False
        
        self.root.mainloop()
        
    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        
        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg="green")
            
    
    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            if self.counter == 0:
                cps = 0; cpm = 0
            else:
                cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            if self.counter == 0:
                wps = 0; wpm = 0
            else:
                wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed:  {cps:.2f} CPS {cpm:.2f} CPM {wps:.2f} WPS {wpm:.2f} WPM")
            
        
    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: 0.00 CPS 0.00 CPM 0.00 WPS 0.00 WPM")
        self.randomSentence()
        self.input_entry.delete(0, tk.END)
    
    
    def randomSentence(self):
        level = self.difficulty_var.get()
        if level == "easy":
            random_text =  easySentence()
        elif level == "medium":
            random_text = mediumSentence()
        else:
            random_text = hardSentence()
        
        self.sample_label.config(text=random_text)
        
    def changeDifficulty(self, event):
        self.randomSentence()
    
TypeSpeedGUI()