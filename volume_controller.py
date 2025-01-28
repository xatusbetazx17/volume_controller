#!/usr/bin/env python3
import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import threading

class SteamDeckVolumeControl:
    def __init__(self, root):
        self.root = root
        self.root.title("Steam Volume Lock")
        self.root.geometry("400x250")
        self.root.configure(bg="#1a1a1a")
        
        self.target_volume = 50  # Default
        self.is_locked = False
        self.running = True
        
        # Steam Deck-inspired styling
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TScale', background='#1a1a1a', troughcolor='#2d2d2d')
        self.style.configure('TButton', font=('Arial', 12), padding=6)
        self.style.map('TButton', background=[('active', '#0078d4')])
        
        self.create_widgets()
        self.start_volume_watcher()

    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg="#1a1a1a")
        header.pack(pady=10)
        
        tk.Label(header, text="🔊 Steam Volume Lock", font=('Arial', 16, 'bold'), 
                bg="#1a1a1a", fg="white").pack()
        
        # Volume Slider
        slider_frame = tk.Frame(self.root, bg="#1a1a1a")
        slider_frame.pack(pady=15)
        
        self.slider = ttk.Scale(slider_frame, from_=0, to=100, length=300,
                               command=self.update_volume_display)
        self.slider.set(self.target_volume)
        self.slider.pack()
        
        self.volume_display = tk.Label(slider_frame, text="50%", font=('Arial', 14),
                                      bg="#1a1a1a", fg="white")
        self.volume_display.pack()
        
        # Control Buttons
        btn_frame = tk.Frame(self.root, bg="#1a1a1a")
        btn_frame.pack(pady=15)
        
        self.lock_btn = ttk.Button(btn_frame, text="🔒 Lock Volume", 
                                  command=self.toggle_lock)
        self.lock_btn.pack(side=tk.LEFT, padx=10)
        
        ttk.Button(btn_frame, text="❌ Exit", command=self.clean_exit).pack(side=tk.RIGHT)

    def update_volume_display(self, value):
        self.target_volume = int(float(value))
        self.volume_display.config(text=f"{self.target_volume}%")
        if self.is_locked:
            os.system(f"pactl set-sink-volume @DEFAULT_SINK@ {self.target_volume}%")

    def toggle_lock(self):
        self.is_locked = not self.is_locked
        if self.is_locked:
            self.lock_btn.config(text="🔓 Unlock Volume")
            self.slider.config(state="disabled")
            messagebox.showinfo("Volume Locked", "Volume is now locked at current level!")
        else:
            self.lock_btn.config(text="🔒 Lock Volume")
            self.slider.config(state="normal")
        self.set_volume(self.target_volume)

    def set_volume(self, level):
        os.system(f"pactl set-sink-volume @DEFAULT_SINK@ {level}%")

    def start_volume_watcher(self):
        def watcher():
            while self.running:
                if self.is_locked:
                    current = int(os.popen("pactl get-sink-volume @DEFAULT_SINK@ | grep -oP '\\d+%' | head -n1").read().strip('%'))
                    if current != self.target_volume:
                        self.set_volume(self.target_volume)
                self.root.update()
                self.root.after(1000)
        threading.Thread(target=watcher, daemon=True).start()

    def clean_exit(self):
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SteamDeckVolumeControl(root)
    root.mainloop()
