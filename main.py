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
        img = PhotoImage(file='gundam.png')
        self.root.iconphoto(True, img)
        
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
       
        
        self.sample_label = customtkinter.CTkLabel(self.frame, text="", font=("Helvetica", 24), wraplength=600, justify="center", height=140)
        self.sample_label.pack(padx=30, pady=10)
        self.randomSentence()
        
        self.input_entry = customtkinter.CTkEntry(self.frame, width=600, font=("Helvetica", 28), placeholder_text="lets roll...", takefocus=True)
        self.input_entry.focus_set()
        self.input_entry.pack(padx=30, pady=20, ipady=15, ipadx=15)
        self.input_entry.bind("<KeyRelease>", self.start)
        
        self.metrics_frame = customtkinter.CTkFrame(self.frame)
        self.metrics_frame.pack(pady=20)

        self.CPS = customtkinter.CTkLabel(self.metrics_frame, text="CPS", font=("Helvetica", 16))
        self.CPS.grid(row =0, column=0, padx=20, pady=5)
        self.CPM = customtkinter.CTkLabel(self.metrics_frame, text="CPM", font=("Helvetica", 16))
        self.CPM.grid(row =0, column=1, padx=20, pady=5)
        self.WPS = customtkinter.CTkLabel(self.metrics_frame, text="WPS", font=("Helvetica", 16))
        self.WPS.grid(row =0, column=2, padx=20, pady=5)
        self.WPM = customtkinter.CTkLabel(self.metrics_frame, text="WPM", font=("Helvetica", 16))
        self.WPM.grid(row =0, column=3, padx=20, pady=5)
        
        self.CPS1 = customtkinter.CTkEntry(self.metrics_frame, placeholder_text="0.00", font=("Helvetica", 16), width=55, justify="center")
        self.CPS1.grid(row =1, column=0, padx=20, pady=5)
        self.CPM1 = customtkinter.CTkEntry(self.metrics_frame, placeholder_text="0.00", font=("Helvetica", 16), width=55, justify="center")
        self.CPM1.grid(row =1, column=1, padx=20, pady=5)
        self.WPS1 = customtkinter.CTkEntry(self.metrics_frame, placeholder_text="0.00", font=("Helvetica", 16), width=55, justify="center")
        self.WPS1.grid(row =1, column=2, padx=20, pady=5)
        self.WPM1 = customtkinter.CTkEntry(self.metrics_frame, placeholder_text="0.00", font=("Helvetica", 16), width=55, justify="center")
        self.WPM1.grid(row =1, column=3, padx=20, pady=5)
        
        
        # self.metrics_labels = ["CPS", "CPM", "WPS", "WPM"]
        # self.metric_entries = {}

        # for i, metric_label in enumerate(self.metrics_labels):
        #     self.label = customtkinter.CTkLabel(self.metrics_frame, text=metric_label, font=("Helvetica", 16))
        #     self.label.grid(row=0, column=i, padx=20, pady=5)
            
        #     self.entry = customtkinter.CTkEntry(self.metrics_frame, placeholder_text="0.00", width=70, font=("Helvetica", 16), state="disabled")
        #     self.entry.grid(row=1, column=i, padx=20, pady=5)
        #     self.metric_entries[metric_label] = self.entry
            
            
        # self.speed_label = customtkinter.CTkLabel(self.frame, text="Speed: 0.00 CPS || 0.00 CPM || 0.00 WPS || 0.00 WPM", font=("Helvectica", 18))
        # self.speed_label.pack(padx=40, pady=20)
        

        self.reset_button = customtkinter.CTkButton(self.frame, text="Reset", command=self.reset, font=("Helvetica", 18))
        self.reset_button.pack(padx=20, pady=20)

        
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
            

            self.CPS1.configure(placeholder_text = f"{cps:.2f}")
            self.CPM1.configure(placeholder_text = f"{cpm:.2f}")
            self.WPS1.configure(placeholder_text = f"{wps:.2f}")
            self.WPM1.configure(placeholder_text = f"{wpm:.2f}")
            
                        
            # self.speed_label.configure(text=f"Speed:  {cps:.2f} CPS || {cpm:.2f} CPM || {wps:.2f} WPS || {wpm:.2f} WPM")
            
        
    def reset(self):
        self.running = False
        self.counter = 0
        # self.speed_label.configure(text="Speed: 0.00 CPS || 0.00 CPM || 0.00 WPS || 0.00 WPM")
        self.randomSentence()
        self.input_entry.focus_set()
        self.input_entry.configure(fg_color="#343638")
        self.input_entry.delete(0, tk.END)
        
        self.CPS1.configure(placeholder_text = "0.00")
        self.CPM1.configure(placeholder_text = "0.00")
        self.WPS1.configure(placeholder_text = "0.00")
        self.WPM1.configure(placeholder_text = "0.00")
        
    
    
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
