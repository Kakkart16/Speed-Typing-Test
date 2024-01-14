import tkinter as tk
from tkinter import ttk
import time
import threading
import random
from tkinter import PhotoImage
from text import easySentence, mediumSentence, hardSentence
from sentences import easy_paragraph, medium_paragraph, hard_paragraph

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class TypeSpeedGUI:
        
    def __init__(self):
        
        self.root = customtkinter.CTk()
        self.root.title("Typing Speed Appliacation")
        self.root.geometry("800x600")
        
        # self.root.iconbitmap('gundam.png')
        
        self.frame = customtkinter.CTkFrame(master = self.root)
        
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        
        self.difficulty = customtkinter.StringVar(value="easy") 
        difficulty_menu = customtkinter.CTkComboBox(
            self.frame, 
            values=["easy", "medium", "hard"],
            variable = self.difficulty,
            command=self.changeDifficulty
        )
        difficulty_menu.pack(padx=30, pady=30)
        # difficulty_menu.bind('<<ComboBoxSelected>>',self.changeDifficulty)
       
        
        self.sample_label = customtkinter.CTkLabel(self.frame, text="", font=("Helvetica", 24), wraplength=600, justify="center")
        self.sample_label.pack(padx=30, pady=20)
        self.randomSentence()
        
        self.input_entry = customtkinter.CTkEntry(self.frame, width=600, font=("Helvetica", 28), placeholder_text="lets roll...", takefocus=True)
        self.input_entry.focus_set()
        self.input_entry.pack(padx=30, pady=20, ipady=15, ipadx=15)
        self.input_entry.bind("<KeyRelease>", self.start)
        
        self.speed_label = customtkinter.CTkLabel(self.frame, text="Speed: 0.00 CPS || 0.00 CPM || 0.00 WPS || 0.00 WPM", font=("Helvectica", 18))
        self.speed_label.pack(padx=40, pady=20)
        

        self.reset_button = customtkinter.CTkButton(self.frame, text="Reset", command=self.reset, font=("Helvetica", 18))
        self.reset_button.pack(padx=20, pady=30)

        
        self.counter = 0
        self.running = False
        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if event.keycode not in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()

        current_text = self.sample_label.cget('text')
        entered_text = self.input_entry.get()

        if not current_text.startswith(entered_text):
            self.input_entry.configure(fg_color="#FF2400")  
        else:
            self.input_entry.configure(fg_color="black")  

        if entered_text == current_text:
            self.running = False
            self.input_entry.configure(fg_color="green")  
    
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
            self.speed_label.configure(text=f"Speed:  {cps:.2f} CPS || {cpm:.2f} CPM || {wps:.2f} WPS || {wpm:.2f} WPM")
            
        
    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.configure(text="Speed: 0.00 CPS || 0.00 CPM || 0.00 WPS || 0.00 WPM")
        self.randomSentence()
        self.input_entry.focus_set()
        self.input_entry.configure(fg_color="#1a1a1a")
        self.input_entry.delete(0, tk.END)
    
    
    def randomSentence(self):
        level = self.difficulty.get()
        if level == "easy":
            random_text =  easy_paragraph()
            
        elif level == "medium":
            random_text = medium_paragraph()
            
        else:
            random_text = hard_paragraph()
        
        self.sample_label.configure(text=random_text)
       
 
    def changeDifficulty(self, event):
        print("difficulty changed")
        self.randomSentence()
   

# TypeSpeedGUI()
    
if __name__ == "__main__":
    TypeSpeedGUI()
